# 🚀 Docker-Kubernetes Load Balancer

This project is a full-stack web application composed of:

- **Frontend**: Angular
- **Backend**: Django + GraphQL
- **Database**: PostgreSQL
- **Dockerized**: All services run with Docker Compose


---

## 📁 Project Structure

```
docker-kubernetes-load-balancer/
├── backend/        # Django backend
├── frontend/       # Angular frontend
├── docker-compose.yml
|__ k8s/
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
git clone https://github.com/Hzekrii/docker-kubernetes-load-balancer.git
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
 **Docker** (doit être démarré pour exécuter les commandes)
2. **Minikube** (cluster Kubernetes local)
3. **kubectl** (outil de gestion Kubernetes)

> 💡 Si Minikube n'est pas installé, suivez les instructions officielles : [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)

Si kubernetes n'est pas installé suivez les instructions
 **kubectl** | [Installation](https://kubernetes.io/docs/tasks/tools/)

## Démarrer le cluster local 
```bash
minikube start --driver=docker
```

## loader les images (apres Build and run the application dans les anciennes etapes)
```bash
eval $(minikube docker-env)
```

```bash
 minikube image load docker-kubernetes-load-balancer-frontend:latest
 ```

```bash
 minikube image load docker-kubernetes-load-balancer-backend:latest
 ```

```bash
 docker pull postgres:16
 ```
## lister les images dans minikube 
 ```bash
 docker images
 ```
 il faut avoir : 

 REPOSITORY                                       TAG       IMAGE ID       CREATED         SIZE
docker-kubernetes-load-balancer-frontend         latest    f0ed3584e24f   28 hours ago    4.21GB
docker-kubernetes-load-balancer-backend          latest    fe639427045c   34 hours ago    1.82GB
postgres                                         16        2e7c735993bf   2 weeks ago     617MB



## Appliquer les configurations Kubernetes

```bash
kubectl apply -f k8s/
```
## consulter les pods et les services 

```bash
kubectl get pods 
``` 
( les pods faut il etre en etat running )

NAME                                   READY   STATUS    RESTARTS   AGE
backend-deployment-55bb68bff4-4g5vz    1/1     Running   0          54m
backend-deployment-55bb68bff4-4q2dq    1/1     Running   0          54m
backend-deployment-55bb68bff4-8dxb8    1/1     Running   0          54m
backend-deployment-55bb68bff4-fzf99    1/1     Running   0          54m
frontend-deployment-679d8b8f59-njn66   1/1     Running   0          54m
postgres-deployment-995596fb8-274pg    1/1     Running   0          54m

```bash
kubectl get svc
```
il faut avoir les service backend  frontend-service et postgres-service


## Accéder à l'application

# Backend 
kubectl port-forward svc/backend 8000:8000


# Frontend
minikube service frontend-service --url

# puis acceder a l'url generer 

