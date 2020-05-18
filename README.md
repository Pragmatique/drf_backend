# Introduction

Backend side for common web application. Django + Django Rest Framework, API endpoint.

# Developer Guide

## Getting Started

### Data base.
For this project I use PostgreSQL DB, so to run project you have to raise PostgreSQL DB on your PC.
I've used default settings:
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432'

If you don't want to use Postgres for demonstration project, you can change configuration in the settings.py
and pick DB you like more. As for me, SQLite for such kind of project is enough.

### Initialize the project

Clone project
Go to the project folder and create virtual environment.
Hope you are able to do it with:
pip install virtualenv
virtualenv venv
in the project folder
After that activate environment with run activation script:
{folder link}/venv/scripts/activate
for me in Windows it looks like C:\Users\root\PycharmProjects\drf_backend\venv\scripts\activate

Install dependencies:
pip install -r requirements.txt

Migrate, create a superuser, and run the server:
cd drf_shop
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver

### Feature with email verification

For some reason Google not allow me to use gmail.smpt, so I've just emulate work with mail
with smtplib:
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

Due to issues with mail server, I had to write my own verification
and did not use more comfortable for this task library - allauth
After registration I send fake mail with verification link (only for demonstration).
To confirm mail I copied link from command prompt and inserted to browser.
To monitor fake mails I ran:
python -m smtpd -n -c DebuggingServer localhost:1025

![Alt text](mail_emulation.jpg?raw=true "mail_emulation")
