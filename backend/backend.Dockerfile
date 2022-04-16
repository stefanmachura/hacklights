FROM python:3.10-slim

RUN apt update && apt upgrade -y
RUN apt install wait-for-it -y

RUN rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod a+x backend-entrypoint.sh

RUN ls

ENTRYPOINT [ "./backend-entrypoint.sh" ]
