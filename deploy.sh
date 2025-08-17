#!/bin/bash
echo "Deploying trading bot..."

docker-compose down
docker-compose up --build -d

echo "Bot deployed 🚀"
