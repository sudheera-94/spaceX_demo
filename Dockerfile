FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --update sqlite
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./spaceX_starlink_add /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*
RUN chmod 777 /app/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
RUN chown -R user:user /app
USER user

CMD ["entrypoint.sh"]