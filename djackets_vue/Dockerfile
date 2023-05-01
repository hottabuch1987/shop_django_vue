FROM node:16-alpine3.16

WORKDIR /usr/src/app

COPY . /usr/src/app
COPY package.json /app/package.json

RUN npm install

EXPOSE 8080

CMD npm run serve

