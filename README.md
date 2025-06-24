# 🚀 Docker-Kubernetes Load Balancer

This project is a full-stack web application composed of:

- **Frontend**: Angular (Nx workspace)
- **Backend**: Django + GraphQL
- **Database**: PostgreSQL
- **Dockerized**: All services run with Docker Compose

> 🛠 Kubernetes setup will be added later.

---

## 📁 Project Structure

```
docker-kubernetes-load-balancer/
├── backend/        # Django backend
├── frontend/       # Angular (Nx) frontend
├── docker-compose.yml
└── README.md
```

---

## 🧰 Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/docker-kubernetes-load-balancer.git
cd docker-kubernetes-load-balancer
```

### 2. Build and run the application

```bash
docker compose up --build
```

This will:
- Reset Nx cache
- Install frontend dependencies (cached)
- Apply backend Django migrations
- Start all services

---

## 🌐 Access Points

- Frontend: [http://localhost:4200](http://localhost:4200)
- Backend (GraphQL): [http://localhost:8000](http://localhost:8000)

---

## 🧼 Shutdown the Services

```bash
docker compose down
```

> The database data and node modules are persisted in Docker volumes.

---

## 🗂 Docker Volumes Used

- `postgres_data`: Saves PostgreSQL data
- `frontend_node_modules`: Caches frontend dependencies

These volumes ensure data is **not lost** when using `docker compose down`.

---

## 📌 Note

The frontend uses `npx nx reset` on every container start to avoid `.nx` caching issues.

---

## 🚧 Kubernetes

Kubernetes configuration will be added later in this repo.

---
