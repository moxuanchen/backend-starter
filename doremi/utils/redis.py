import redis


def configure_redis(app):
    params = {
        "host": app.config["REDIS_HOST"],
        "port": app.config["REDIS_PORT"],
        "db": app.config["REDIS_DB_INDEX"]
    }

    app.config["REDIS"] = redis.StrictRedis(**params)


def set_to_redis(instance, key, value, expire=None):
    if expire:
        return instance.setex(key, expire, value)
    return instance.set(key, value)


def get_from_redis(instance, key):
    return instance.get(key)
