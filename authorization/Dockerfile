FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests
ADD authorization.py /home/authorization.py
WORKDIR /home/
CMD python3 authorization.py

