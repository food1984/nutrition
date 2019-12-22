FROM python:3.7

COPY app.py .
COPY database.py .
COPY requirements.txt .
COPY get_govt_data .

RUN pip install -r requirements.txt
