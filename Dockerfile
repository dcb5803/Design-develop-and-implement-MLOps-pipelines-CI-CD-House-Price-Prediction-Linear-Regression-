# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir gradio scikit-learn pandas

# Expose Gradio default port
EXPOSE 7860

# Run the app
CMD ["python", "app.py"]
