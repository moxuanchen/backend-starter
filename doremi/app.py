import sys
import logging

from doremi.utils import configure_redis
from doremi.settings import get_config_env
from doremi.api.app.api import app_blueprint
from flask import Flask, render_template
from doremi.extensions import (
    bcrypt,
    cache,
    csrf_protect,
    db,
    flask_static_digest,
    login_manager,
    migrate,
)


def create_app(config_object=get_config_env()):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    configure_logger(app)
    configure_redis(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    flask_static_digest.init_app(app)


def register_blueprints(app):
    app.register_blueprint(app_blueprint)


def register_errorhandlers(app):

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template(f"{error_code}.html"), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
