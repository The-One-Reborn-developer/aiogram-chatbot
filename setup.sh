#!/bin/bash

echo "Installing ollama software..."
curl -fsSL https://ollama.com/install.sh | sh

echo "Pulling gemma2 model..."
ollama pull gemma2

echo "Making sure ollama is served..."
ollama serve

echo "Creating a model from Modelfile..."
ollama create aiogramhelper -f ./Modelfile

echo "Installation completed."