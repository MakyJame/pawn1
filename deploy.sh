#!/bin/bash
set -e 

echo "Pull latest code..."
git pull origin nginx/host

echo "Pull latest images..."
docker compose pull

echo "Start container..."
docker compose up -d 

echo "Done"

docker ps

