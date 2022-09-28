# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /sample_blog
COPY requirements.txt /sample_blog/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN pytohn manage.py migrate
RUN python manage.py loaddata prod_group
RUN python manage.py loaddata dummy_user
RUN python manage.py loaddata dummy_basic
COPY . /sample_blog/