FROM python:3.10-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./run.sh

CMD ["./run.sh"]
