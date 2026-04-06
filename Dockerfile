FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn transformers torch requests

CMD ["python", "main.py"]