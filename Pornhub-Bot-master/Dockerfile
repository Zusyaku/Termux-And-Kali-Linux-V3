FROM python:3.9.5-buster

RUN apt-get update && apt-get upgrade -y

#Installing Requirements
RUN apt-get install -y ffmpeg python3-pip opus-tools

#Updating pip
RUN python3.9 -m pip install -U pip

COPY . .

RUN python3.9 -m pip install -U -r requirements.txt

CMD python3 bot.py