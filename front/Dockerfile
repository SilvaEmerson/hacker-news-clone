FROM node:8-alpine

COPY . /mnt/front

WORKDIR /mnt/front

RUN npm i &&\
    npm run-script build &&\
    rm -r node_modules &&\
    npm i -g http-server

WORKDIR ./build

CMD http-server -p ${FRONT_PORT}
