from orator import DatabaseManager, Schema, Model

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": "db",
        "database": "example",
        "user": "daniel",
        "password": "nihao",
        "prefix": "",
        "port": 5432,
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)