FROM python:3.7.4-alpine

COPY . /mnt/back

WORKDIR /mnt/back

ARG DJANGO_KEY_ARG

ENV DJANGO_KEY ${DJANGO_KEY_ARG}

RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                libffi-dev \
                libressl-dev \
        ; \
        pip install --upgrade pip; \
        pip install --no-cache-dir -r requirements.txt; \
        apk del .build-deps; \
        python manage.py makemigrations; \
        python manage.py migrate;

CMD hypercorn hackernewsclone.asgi:application -b 0.0.0.0:${BACK_PORT} -w ${BACK_N_WORKERS}
