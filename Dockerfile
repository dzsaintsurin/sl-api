FROM python:3.10.10-alpine3.17

WORKDIR /app

COPY sl-api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "/app/sl-api/main.py"]
