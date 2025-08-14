from flask import Flask, render_template, request, Response, jsonify
import ollama as ol
import json

app = Flask(__name__)

chat_model = None

@app.route('/', methods=['GET', 'POST'])
def home():
	installed_models = ol.list().models
	installed_models = [m.model for m in installed_models]
	
	if request.method == 'POST':
		# For AJAX requests, return JSON
		if request.headers.get('Content-Type') == 'application/json':
			data = request.get_json()
			prompt = data.get('prompt')
			chat_model = data.get('model')
			
			if prompt and chat_model:
				return Response(stream_response(prompt, chat_model), 
							  mimetype='text/plain')
			return jsonify({'error': 'Missing prompt or model'})
	
	# For regular form submissions, render the page
	return render_template('index.html', models=installed_models)

@app.route('/stream', methods=['POST'])
def stream_chat():
	data = request.get_json()
	prompt = data.get('prompt')
	chat_model = data.get('model')
	
	if prompt and chat_model:
		return Response(stream_response(prompt, chat_model), 
					  mimetype='text/plain')
	return jsonify({'error': 'Missing prompt or model'})

def stream_response(prompt, model):
	try:
		response = ol.chat(
			model=model,
			messages=[{"role": "user", "content": prompt}],
			stream=True
		)
		
		for chunk in response:
			if hasattr(chunk, 'message') and hasattr(chunk.message, 'content'):
				content = chunk.message.content
			elif isinstance(chunk, dict):
				message = chunk.get('message', {})
				if isinstance(message, dict):
					content = message.get('content', '')
				else:
					content = str(message)
			else:
				content = str(chunk)
			
			if content:
				yield content
				
	except Exception as e:
		yield f"Error: {str(e)}"



if __name__ == '__main__':
	# Enable host binding for Docker container
	app.run(host='0.0.0.0', port=5000, debug=False)
