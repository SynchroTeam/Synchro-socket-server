FROM ubuntu:20.04

# Install SFTP and other linux modules
RUN apt-get update && apt-get install -y openssh-server && \
    mkdir /var/run/sshd && \
    apt-get install augeas-tools -y && \
    augtool --autosave 'set /files/etc/ssh/sshd_config/PasswordAuthentication yes' && \
    addgroup sftp-only && \
    apt install nano -y


COPY ./Receiver/ubuntu/sshd_config  /etc/ssh/sshd_config

# to not list all users home directories
RUN chmod 701 /home

WORKDIR /code/
COPY . .

# Installing Python via PPA and pip3
RUN apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt update && \
    apt install python3.9 -y && \
    apt install python3-pip -y

RUN python3 -m pip install -r requirements.txt