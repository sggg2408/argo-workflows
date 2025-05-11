FROM python:3.11-slim

RUN pip install metaflow boto3

WORKDIR /app
COPY analyticsUpdateJob.py .

ENTRYPOINT ["python", "analyticsUpdateJob.py", "run"]

