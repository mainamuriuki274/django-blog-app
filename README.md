# BLOGGR

## Description
This repository implemented using Django, contains the API endpoint and models for the BLOGGR project.
- [Requirements](#requirements)
 - [Local Development](#local-development)
    - [Env setup](#env-setup)
    - [Project setup](#project-setup)
      - [Manual setup](#manual-setup)
    - [Running the app](#running-the-app)

## Requirements
* python 3
* pipenv
  - If you're on MacOS, you can install Pipenv easily with Homebrew:
    ```bash
    brew install pipenv
    ```
  - Debian Buster+:
    ```bash
    sudo apt install pipenv
    ```
  - Fedora:
    ```bash
    sudo dnf install pipenv
    ```
  - FreeBSD:
    ```bash
    pkg install py36-pipenv
    ```

## Local Development
### Env Setup
## Run the following commands in your terminal
* Clone the repo:
    ```bash
    git clone https://github.com/mainamuriuki274/django-blog-app.git
    ```
* Navigate to the cloned folder:
    ```bash
    cd django-blog-app/
    ```
* Inorder to create a virtual environment, run the command below which will create the virtual environment and create a pipfile for package requirements
    ```bash
    pipenv shell
    ```
* To install the packages in your virtual environment, run
    ```bash
    pipenv install
    ```
* Create a .env file to where you'll put the environment variables
    ```bash
    touch .e
    ```

We Currently use the following env variables:  
 + DATABASE_URL - Used by [dj_database_url](https://github.com/kennethreitz/dj-database-url#url-schema) to connect to the database.  
 + SECRET_KEY - String of random characters used to provide cryptographic signing for [Django](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-SECRET_KEY) projects.

### Project setup
#### Manual setup
- Create a database and add its url to your project environment. eg `DATABASE_URL=postgresql://<user>:<password>@localhost:5432/<db>`
- Create and activate a virtual environment - we recommend using [pipenv](https://github.com/pypa/pipenv) for this by running `pipenv shell`
- Install the project dependencies stored in [Pipfile](/Pipfile). Run
    ```bash
    pipenv install --dev
    ```
- Run migrations:
    ```bash
    python manage.py migrate
    ```

### Running the app
- Create a Superuser account:
    ```bash
    python manage.py createsuperuser
    ```
- To run tests:
    ```bash
    pytest
    ```
- Run the app:
    ```bash
    python manage.py runserver
    ```
- Yay! Congratulations your app should be running at [http://127.0.0.1:8000/app/api/v1/graphql/](http://127.0.0.1:8000/app/api/v1/graphql/)
- You can now log into the admin dashboard on [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
