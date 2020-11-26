# GraphQL with FastAPI, Orator and PostgreSQL
An example of using GraphQL in Python 3 FastAPI.

## migrations
Holds the table fields definitions.
- You can add table with orator command `orator make:model <table_name> -m`.
- Then you add or edit the fields inside generated files and define primary key or foreign key.
- To apply migrations `orator migrate -c db.py`

## models
Holds the db table as a .py file, and each file let you interact with db without SQL instead of functions just like ORM did. To access the functions simply `<table_name>.py.save()` for instance.
- You define the relations between tables (one-to-many, one-to-one, many-to-many) 

## db.py
Define connections to your database.

## main.py
Define FastAPI endpoints.

## schema.py
Define GraphQL Schema (Query and Mutation).

## serializers.py
Define meta for GraphQL Model that is used by Query and Mutation for referencing to the db tables. It also shows how to use PyDantic as validation system.

## How to try
Install Docker, docker-compose and run `docker-compose up`. It will run at `localhost:7000/graphiql`.
You can manage the db with adminer at `localhost:8080`.