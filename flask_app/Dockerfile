FROM python:3.9-slim

WORKDIR /app

EXPOSE 5000

COPY ./requirements.txt /app

COPY ./entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

COPY . /app

CMD ["/bin/bash", "entrypoint.sh"]
