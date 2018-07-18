dev:
	python manage.py runserver -v2

test:
	DEBUG=False pytest -s -vv --cov=. .

docker-compose-up:
	docker-compose -f docker-compose-dev.yml up

update:
	git pull
	docker-compose build app celery celery_beat
	docker-compose run app python manage.py migrate
	docker-compose run app python manage.py collectstatic --noinput
	docker-compose up -d --force-recreate --remove-orphans
	docker system prune -f

backup:
	mkdir -p /home/deployment/backup/
	docker-compose run app python manage.py dbbackup -z
	mv /home/deployment/git/*.psql* /home/deployment/backup/
	docker system prune -f

clean_queue:
	docker-compose stop celery celery_beat
	docker-compose run app redis-cli -h redis flushall
	docker system prune -f
	docker-compose start celery celery_beat
