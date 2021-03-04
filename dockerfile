FROM ubuntu:20.04

# Update linux
RUN apt-get update && apt-get install

WORKDIR /code/
COPY . .

# Installing Python via PPA and pip3
RUN apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt update && \
    apt install python3.9 -y && \
    apt install python3-pip -y

RUN python3 -m pip install -r requirements.txt