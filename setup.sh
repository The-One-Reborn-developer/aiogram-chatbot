#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status.

echo "Installing ollama software..."
curl -fsSL https://ollama.com/install.sh | sh

echo "Launching ollama server..."
ollama serve &  # Run ollama serve in the background.

# Wait for the Ollama server to be fully up before proceeding.
echo "Waiting for Ollama server to start..."
sleep 5  # Adjust sleep time as necessary.

# Check if the Ollama server is running and accessible.
if ! curl -s http://127.0.0.1:11434/health > /dev/null; then
    echo "Ollama server failed to start. Exiting..."
    exit 1
fi

echo "Pulling llama3 model..."
if ! ollama pull llama3; then
    echo "Failed to pull llama3 model. Exiting..."
    exit 1
fi

echo "Pulling bge-m3 embedding model..."
if ! ollama pull bge-m3; then
    echo "Failed to pull bge-m3 embedding model. Exiting..."
    exit 1
fi

echo "Saving data from PDF to ChromaDB..."
python3 populate_database.py

echo "Setup completed."

echo "Launching bot..."
python3 main.py
