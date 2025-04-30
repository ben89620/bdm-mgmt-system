FROM node:lts-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm install @vitejs/plugin-vue

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
