#Build from Ubunutu
FROM ubuntu:16.04

MAINTAINER Brianna Boyce "brieboyce@gmail.com"

#Install Pip
RUN  apt-get update -y && \
 apt-get install -y python-pip python-dev

#Grab the requirements - currently includes Flask
COPY ./requirements.txt /todolist/requirements.txt

#Working directory is todolist
WORKDIR /todolist

#Install Python dependencies with Pip
RUN pip install -r requirements.txt

#Copy everything in todolist
COPY . /todolist

#use python command
ENTRYPOINT [ "python" ]

#Run python app
CMD [ "todolist.py" ]
