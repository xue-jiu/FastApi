
TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "127.0.0.1",
                "port": "3306",
                "user": "your_oracle_username",
                "password": "Plq@c123",
                "database": "fast",
            },
        },
    },
    "apps": {
        "models": {
            "models": ["DB.Article"],
            "default_connection": "default",
        },
    },
}
