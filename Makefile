migrate:
	python classiclass/manage.py makemigrations users posts tags
	python classiclass/manage.py migrate
