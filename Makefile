up:
	docker-compose up -d

down:
	docker-compose down
	
restart:
	docker-compose restart

build:
	docker-compose up --build -d

logs:
	docker-compose logs -f --tail=100

