up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs app -f

migrate-alembic:
	docker compose exec app alembic revision --autogenerate
	docker compose exec app alembic upgrade head

pytest:
	docker compose exec app pytest
	
hard-restart:
	docker compose down -v
	docker rmi mega-capital-derbit-app
	rm -rf alembic/versions
	mkdir alembic/versions
	make up
	sleep 2
	make migrate-alembic

open-bash:
	docker compose exec -it "app" bash