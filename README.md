# Ollama Flask App - Containerized

A containerized Flask web application that provides a streaming interface for interacting with Ollama models.

## 🚀 Features

- **Real-time streaming** responses from Ollama models
- **Markdown rendering** with math expressions support
- **Thinking process** toggle (show/hide LLM reasoning)
- **Responsive UI** with scroll-to-top functionality
- **Docker containerized** for easy deployment
- **Health checks** and monitoring ready

## 📦 Quick Start with Docker

### Option 1: Docker Compose (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd ollama-flask

# Start both Flask app and Ollama service
docker-compose up -d

# Access the application
open http://localhost:5000
```

### Option 2: Docker Build & Run

```bash
# Build the image
docker build -t ollama-flask .

# Run the container
docker run -d \
  --name ollama-flask-app \
  -p 5000:5000 \
  --restart unless-stopped \
  ollama-flask

# Access the application
open http://localhost:5000
```

## 🔧 Configuration

### Environment Variables

- `FLASK_ENV`: Set to `production` for production deployment
- `FLASK_DEBUG`: Set to `0` to disable debug mode
- `OLLAMA_HOST`: Ollama server host (default: localhost)

### Docker Compose Services

1. **ollama-flask**: The main Flask application
   - Port: 5000
   - Health checks enabled
   - Auto-restart on failure

2. **ollama**: Ollama service (optional)
   - Port: 11434
   - Persistent data storage
   - GPU support ready (uncomment in docker-compose.yml)

## 🛠️ Development

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python index.py
```

### Building Custom Images

```bash
# Build with custom tag
docker build -t your-registry/ollama-flask:latest .

# Push to registry
docker push your-registry/ollama-flask:latest
```

## 📊 Health Monitoring

The application includes health checks:

```bash
# Check container health
docker ps

# View health check logs
docker inspect ollama-flask-app
```

## 🔒 Security Features

- Non-root user execution
- Minimal attack surface
- Read-only template mounting
- Network isolation

## 🚀 Production Deployment

### Using Docker Compose

```bash
# Production deployment
docker-compose -f docker-compose.yml up -d

# Scale if needed
docker-compose up -d --scale ollama-flask=3
```

### Using Docker Swarm

```bash
# Initialize swarm
docker swarm init

# Deploy stack
docker stack deploy -c docker-compose.yml ollama-stack
```

### Using Kubernetes

```bash
# Generate Kubernetes manifests
docker-compose config > k8s-manifest.yml

# Deploy to Kubernetes
kubectl apply -f k8s-manifest.yml
```

## 📝 API Endpoints

- `GET /`: Main application interface
- `POST /stream`: Streaming chat endpoint

## 🔍 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change port in docker-compose.yml
   ports:
     - "5001:5000"  # Use port 5001 instead
   ```

2. **Ollama connection issues**
   ```bash
   # Check Ollama service status
   docker-compose logs ollama
   
   # Restart Ollama service
   docker-compose restart ollama
   ```

3. **Container won't start**
   ```bash
   # Check logs
   docker-compose logs ollama-flask
   
   # Rebuild image
   docker-compose build --no-cache
   ```

## 📈 Performance

- **Memory usage**: ~50MB base container
- **CPU usage**: Minimal (dependent on model inference)
- **Network**: Optimized streaming responses
- **Storage**: Persistent Ollama models via volumes

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Make changes and test with Docker
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.
