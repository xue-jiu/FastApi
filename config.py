
TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "127.0.0.1",
                "port": "3306",
                "user": "root",
                "password": "1111",
                "database": "fast",
            },
        },
    },
    "apps": {
        "models": {
            "models": ["DB.Article","aerich.models"],
            "default_connection": "default",
        },
    },
}
