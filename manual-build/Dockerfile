FROM python:3.7-alpine

WORKDIR /app

RUN pip install Flask

COPY hello.py .

COPY start-app.sh .

CMD ["/bin/sh","start-app.sh"]
