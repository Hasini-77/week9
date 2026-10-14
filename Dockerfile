FROM python:3.9-slim-buster
WORKDIR /app
copy . /app
run pip install --no-cache-dir -r requirements.txt
expose 5000
cmd ["python", "app.py"]