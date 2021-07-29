# fast-tools

fastapi and react application for tools rental application

The solution was built with Fastapi and pydantic with Sqlalchemy, sqlite, Alembic(for migrations).

## How to build

1. Create .env file and using the envexample file and fillout the information for the variables in there before you build the docker image and deploy using docker-compose.

2. Build the docker images using docker-compose

    docker-compose build

## How to run

Run docker-compose to run the docker setup

    docker-compose up

and go to:

    http://localhost:8000

## database migration

When you update the sqlalchmey model then you need to run the alembic to run the database update. You can do it from docker-compose. The final migrations are in the alembic dir.

Make a migration:

    docker-compose run web alembic revision --autogenerate -m "you change note here"

Migrate the database:

    docker-compose run web alembic upgrade head

## Documentation

    swagger - http://localhost:8000/docs
    redoc - http://localhost:8000/redoc
