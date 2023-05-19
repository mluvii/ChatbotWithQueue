FROM python:3.10-slim
WORKDIR /app
COPY ./ChatbotWithQueue /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

# Run wsgi.py when the container launches
CMD ["python", "wsgi.py"]
