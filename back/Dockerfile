FROM python:3.7.4-alpine

COPY . /mnt/back

WORKDIR /mnt/back

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
