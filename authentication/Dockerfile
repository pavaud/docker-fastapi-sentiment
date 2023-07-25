FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests
ADD authentication.py /home/authentication.py
WORKDIR /home/
CMD python3 authentication.py

