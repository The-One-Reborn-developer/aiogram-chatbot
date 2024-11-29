#!/bin/bash

echo "Installing ollama software..."
curl -fsSL https://ollama.com/install.sh | sh

echo "Pulling llama3 model..."
ollama pull llama3

echo "Pulling nomic-embed-text..."
ollama pull nomic-embed-text

echo "Making sure ollama is served..."
ollama serve

echo "Setup completed."