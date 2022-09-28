# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /sample_blog
EXPOSE 8000
COPY requirements.txt /sample_blog/
RUN pip install -r requirements.txt
COPY . /sample_blog/