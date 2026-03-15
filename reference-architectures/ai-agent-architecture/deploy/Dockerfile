# Dockerfile for Agentic AI demo
FROM python:3.10-slim

WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command
CMD ["python", "agent.py"] 
