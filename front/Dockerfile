FROM node:21.5.0-alpine3.19 AS builder
ARG DOMAIN
ENV BACKEND_URL=http://${DOMAIN}/api
WORKDIR /app

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
