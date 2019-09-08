FROM python:3.7.4-alpine

COPY . /mnt/back

WORKDIR /mnt/back

ARG DJANGO_KEY_ARG
ARG POSTGRES_NAME_ARG
ARG POSTGRES_USER_ARG
ARG POSTGRES_PASSWORD_ARG

ENV DJANGO_KEY ${DJANGO_KEY_ARG}
ENV POSTGRES_PASSWORD ${POSTGRES_PASSWORD_ARG}
ENV POSTGRES_NAME ${POSTGRES_NAME_ARG}
ENV POSTGRES_USER ${POSTGRES_USER_ARG}

RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                libffi-dev \
                libressl-dev \
                libpq \
                postgresql-dev \
                musl-dev \
        ; \
        pip install --upgrade pip; \
        pip install --no-cache-dir -r requirements.txt;

CMD hypercorn hackernewsclone.asgi:application -b 0.0.0.0:${BACK_PORT} -w ${BACK_N_WORKERS}
