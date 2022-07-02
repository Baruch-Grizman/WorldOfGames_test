FROM python:3.8.13-slim
COPY . /wog/
WORKDIR ./wog/
RUN apt-get -y update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8777