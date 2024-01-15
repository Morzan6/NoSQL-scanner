FROM node:21.5.0-bookworm
WORKDIR /app

RUN npm i -g @quasar/cli

COPY package.json package.json
RUN npm install

COPY . .
RUN npm run build

EXPOSE 4000
ENTRYPOINT ["quasar", "serve", "dist/spa"]


