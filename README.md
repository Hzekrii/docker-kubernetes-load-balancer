docker-kubernetes-load-balancer

This project is a full-stack web application using:

Frontend: Angular + Nx

Backend: Django with GraphQL

Database: PostgreSQL

Containerization: Docker + Docker Compose

Kubernetes configuration will be added later by a classmate.

🔧 Requirements

Docker & Docker Compose installed

🚀 Getting Started

Clone the project

git clone https://github.com/your-username/docker-kubernetes-load-balancer.git
cd docker-kubernetes-load-balancer

Run the app

docker compose up --build

Wait for the containers to finish building. The app will be accessible at:

Frontend: http://localhost:4200

Backend: http://localhost:8000

Stop the app

docker compose down

Your database and frontend dependencies are persisted with volumes, so data and installs are preserved between runs.

📂 Project Structure

docker-kubernetes-load-balancer/
│
├── backend/ # Django + GraphQL API
├── frontend/ # Angular + Nx frontend
├── docker-compose.yml
└── README.md # You're here

🧠 Notes

User accounts and database data are saved across restarts.

No need to manually delete .nx folder anymore.

Volumes handle node_modules and PostgreSQL data persistence.

☁️ Kubernetes (Coming Soon)

Kubernetes deployment instructions will be added by another team member.
