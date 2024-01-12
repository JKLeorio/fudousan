# fudousan

Проект для создания и отображения объявлений о недвижимости.

**УСтановка и запуск**

Установите зависимости python

после установки python
python -m pip install poetry

перемещаемся в дирректорию проекта
poetry install
poetry shell

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
