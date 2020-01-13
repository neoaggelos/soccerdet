FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY soccerdet /app
RUN pip install .

ENTRYPOINT ["manage.py"]
