import os
import yaml


class Config(object):

    DEBUG = True
    CACHE_TYPE = "simple"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "--*--This is a secret key--*--"
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB_INDEX = 1

    def __init__(self):
        APP_DIR = os.path.abspath(os.path.dirname(__file__))
        config_file = os.path.join(APP_DIR, "settings" + '.yaml')
        if os.path.isfile(config_file):
            conf = yaml.load(open(config_file), Loader=yaml.SafeLoader) or {}
            for k, v in conf.items():
                setattr(self, k, v)


class DevConfig(Config):
    """Development configuration"""
    pass


class ProdConfig(Config):
    """Production configuration."""
    DEBUG = False


def get_config_env():
    envs = {
        "dev": DevConfig(),
        "prod": ProdConfig()
    }
    return envs[os.getenv("FLASK_ENV", "dev")]
