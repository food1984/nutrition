FROM python:3.7

COPY nutrition.py .
COPY app .
COPY requirements.txt .
COPY get_govt_data .

RUN pip install -r requirements.txt
