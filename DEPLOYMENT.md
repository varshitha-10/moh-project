# Deployment Guide

## Docker Compose
1. Build and start all services:
   ```sh
   docker-compose up --build
   ```
2. Access frontend at http://localhost:3000 and backend at http://localhost:8000

## Kubernetes (Optional)
- Use Kompose or Helm to convert docker-compose.yml to Kubernetes manifests.
- Example:
  ```sh
  kompose convert
  kubectl apply -f ./
  ```
- Configure secrets, persistent volumes, and ingress as needed.
