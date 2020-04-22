FROM ubuntu:16.04

MAINTAINER Brianna Boyce "brieboyce@gmail.com"

RUN apt-get update -y && \ apt-get install -y python-pip python-dev

COPY ./requirements.txt /todolistApi/requirements.txt

WORKDIR /todolistApi

RUN pip install -r requirements.txt

COPY . /todolistApi

ENTRYPOINT [ "python" ]

CMD [ "todolistApi.py" ]
