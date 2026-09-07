FROM python:3.11-slim

# Install huggingface_hub
RUN pip install --no-cache-dir huggingface_hub

# Create model directory inside container
RUN mkdir -p /models/gemma4

# Copy your Python downloader
COPY main.py /app/main.py

# Set working directory
WORKDIR /app

# Run the downloader when container starts
CMD ["python", "main.py"]
