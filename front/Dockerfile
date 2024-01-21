FROM node:21.5.0-alpine3.19 AS builder
WORKDIR /app
ENV BACKEND_URL="http://localhost/api"

COPY package.json package.json
RUN npm install

COPY . .
RUN npm run build


FROM node:21.5.0-alpine3.19
WORKDIR /app

RUN apk update && apk add bash
RUN npm i -g @quasar/cli

COPY --from=builder /app/dist/spa ./dist/spa


EXPOSE 4000
ENTRYPOINT ["quasar", "serve", "dist/spa", "--history"]
