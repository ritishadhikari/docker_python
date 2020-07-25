FROM python:3.7-slim

RUN apt-get update && apt-get install -y default-mysql-client

RUN mysql --version

RUN pip install Django schedule mysql-connector-python
