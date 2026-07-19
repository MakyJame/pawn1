#!/bin/bash
echo start

echo "Pull latest code"

git pull origin develop

echo "Build new image"

docker compose up -d --build

echo done

echo "Current container"
docker ps

if docker compose up -d
then
 echo "SUCCESS"
else
 echo "FAILED"
 exit 1
fi
