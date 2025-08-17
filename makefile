BOT=trading-bot

.PHONY: build up down logs restart shell

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f $(BOT)

restart: down up

shell:
	docker exec -it $(BOT) /bin/bash
