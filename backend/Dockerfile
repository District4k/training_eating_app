# Use a more recent Python version
FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /opt/app/backend

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port used in docker-compose
EXPOSE 8885

# Start the server
CMD ["python3", "server.py"]