FROM ubuntu:22.04
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get autoremove -y
RUN apt-get install -y python3-pip python3-dev
RUN pip3 install --upgrade pip
RUN pip install pyngrok email
WORKDIR /home/workspace

CMD ["python", "smtp_server.py"]
