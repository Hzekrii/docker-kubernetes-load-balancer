# frontend/Dockerfile
FROM node:18

WORKDIR /app

COPY . .

RUN npm install --force

EXPOSE 4200

CMD ["npm", "run", "start"]
