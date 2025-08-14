from flask import Flask, render_template, request
import ollama as ol

app = Flask(__name__)

chat_model = None

@app.route('/', methods=['GET', 'POST'])
def home():
	installed_models = ol.list().models

	installed_models = [m.model for m in installed_models]

	prompt = None
	if request.method == 'POST':
		prompt = request.form.get('prompt')
		chat_model = request.form.get("model")
		
		if prompt and chat_model:
			response = ol.chat(
				model=chat_model,
				messages=[
					{"role": "user", "content": prompt}
				]
			)

	return render_template('index.html', prompt=prompt, models=installed_models, response=response.message.content)



if __name__ == '__main__':
	app.run(debug=True)
