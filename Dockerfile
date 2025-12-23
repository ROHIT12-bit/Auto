# Use slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies if needed (like ffmpeg or curl)
RUN apt update && apt install -y curl ffmpeg && rm -rf /var/lib/apt/lists/*

# Copy all files to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask (Render expects 8080)
EXPOSE 8080

# Run the Flask app (this will keep container alive)
CMD ["python3", "app.py"]
