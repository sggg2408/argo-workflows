FROM python:3.11-slim

RUN pip install metaflow boto3

WORKDIR /app
COPY flow.py .

ENTRYPOINT ["python", "flow.py", "run"]

