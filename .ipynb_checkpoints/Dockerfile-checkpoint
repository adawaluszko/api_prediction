FROM python:3.11-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY api_prediction.py .
ENV FLASK_APP=api_prediction
EXPOSE 5003
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5003"]
