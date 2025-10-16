FROM python:3.10-slim

WORKDIR /app
COPY app.py .

RUN pip install --no-cache-dir gradio scikit-learn pandas numpy

EXPOSE 7860
CMD ["python", "app.py"]

