FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# Change 'main' below if your file is not named main.py
CMD ["python", "main.py"]