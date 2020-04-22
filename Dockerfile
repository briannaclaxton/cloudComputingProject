FROM ubuntu:16.04

MAINTAINER Brianna Boyce "brieboyce@gmail.com"

RUN  apt-get update -y && \
 apt-get install -y python-pip python-dev

COPY ./requirements.txt /todolist/requirements.txt

WORKDIR /todolist

RUN pip install -r requirements.txt

COPY . /todolist

ENTRYPOINT [ "python" ]

CMD [ "todolist.py" ]
