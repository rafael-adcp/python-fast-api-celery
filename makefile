compose-run:
	docker-compose down && docker-compose up --build

rprado:
	docker build -t fastapi-and-celery . && \
	docker run --name rprado-poc --rm -i -t fastapi-and-celery bash && \
	docker exec -d rprado-poc ls -l