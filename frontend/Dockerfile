FROM node:18

WORKDIR /app

# Install dependencies with cache optimizations
COPY package.json package-lock.json nx.json ./
COPY tsconfig*.json ./
COPY project.json ./

RUN npm install --force && npx nx reset

# Copy rest of the frontend project
COPY . .

EXPOSE 4200

# Run using the fixed package.json script
CMD ["npm", "run", "start"]
