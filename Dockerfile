FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV RUNNING_IN_DOCKER True


RUN mkdir /social_app

WORKDIR /social_app

ADD . /social_app/

RUN pip install -r requirements.txt



