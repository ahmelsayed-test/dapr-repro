FROM node:8-alpine
WORKDIR /usr/src/app
COPY . .
RUN npm install
EXPOSE 3000
CMD [ "node", "--max-http-header-size=66560", "app.js" ]
