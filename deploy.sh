#!/bin/bash

echo start

echo "Pull latest code"

git pull origin main

echo "Build new image"

docker compose up -d --build

echo done

