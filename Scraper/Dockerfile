FROM python:3.10-slim-buster

WORKDIR /python-docker

RUN pip install flask
RUN pip install requests
RUN pip install bs4

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]