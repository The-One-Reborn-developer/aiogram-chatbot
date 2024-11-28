#!/bin/bash

echo "Installing ollama software..."
curl -fsSL https://ollama.com/install.sh | sh

echo "Pulling gemma2 model..."
ollama pull gemma2

echo "Pulling nomic-embed-text..."
ollama pull nomic-embed-text

echo "Making sure ollama is served..."
ollama serve

echo "Creating a model from Modelfile..."
ollama create cryptopaychatbot -f ./Modelfile

npm install -g pnpm

echo "Setup completed."