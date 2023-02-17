FROM python:3.10.10-alpine3.17

WORKDIR /app

# RUN mkdir -p /app/src && cp ../src/requirements.txt /app/src

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "/app/src/main.py"]