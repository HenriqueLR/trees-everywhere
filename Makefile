#makefile
SHELL := /bin/bash

install: dependences static migrate run

dependences:
	pip install -r requirements.txt ;\

run: clean
	./app/manage.py runserver 0.0.0.0:8003 --settings=conf.settings ;\

static:
	./app/manage.py collectstatic --noinput ;\

createsuperuser:
	./app/manage.py createsuperuser ;\

migrate:
	./app/manage.py makemigrations --settings=conf.settings ;\
	./app/manage.py migrate --settings=conf.settings ;\

remove_migrations:
	find . -path "*/migrations/*__pycache__" -not -name "__init__.py" -delete ;\
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete ;\

clean:
	find . -path "*__pycache__*" | xargs rm -rf ;\
	find . -name "*.pyc" | xargs rm -f ;\

clean_db_local:
	find . -name "*.sqlite3" | xargs rm -f

reset_db_local: clean clean_db_local remove_migrations migrate createsuperuser

permissions:
	find . -name "*.sh" | xargs chmod 0755 ;\

statics:
	docker-compose exec app python app/manage.py collectstatic --noinput ;\

migrations_app:
	docker-compose exec app python app/manage.py makemigrations --settings=conf.settings_production ;\
	docker-compose exec app python app/manage.py migrate --settings=conf.settings_production ;\

createsuperuser_app:
	docker-compose exec app python app/manage.py createsuperuser --settings=conf.settings_production ;\

remove_nginx:
	docker rm -f nginx-trees ;\

remove_postgresql:
	docker rm -f postgresql-trees ;\

remove_app:
	docker rm -f trees-everywhere ;\

restartall: remove_postgresql remove_app remove_nginx
	docker-compose up -d ;\

remove:
	docker rm -f $(image) ;\

restart: remove
	docker-compose up --no-deps -d $(service) ;\

build:
	docker-compose up -d ;\

test:
	cd app/ && python manage.py test ;\

doc:
	@sphinx-build -E -W -c docs/source/ -b html docs/source/ docs/build/html

lint:
	flake8 --exit-zero

cov:
	cd app/ &&	coverage run manage.py test && coverage report -m && coverage html && coverage erase   