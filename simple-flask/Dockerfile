FROM python:3.6-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY hello.py .

#Pulls information into image metadata that the image exposes port 5000
EXPOSE 5000

CMD python hello.py
