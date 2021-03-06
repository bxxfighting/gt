import os
import logging
from flask import Flask
from flask import Blueprint

from gt import configs
from account import account_router
from gt import redis
from gt import session


APP_NAME = 'gt'


def create_app():
    app = Flask(APP_NAME)
    app.config.from_object(configs.DefaultConfig)
    config_blueprint(app)
    config_logger(app)
    config_redis(app)
    config_session(app)
    return app


def config_blueprint(app):
    app.register_blueprint(account_router, url_prefix='/api/v1')


def config_logger(app):
    log_dir = './var/log/'
    log_filename = 'flask.log'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    config_dict = {
        'filename': log_dir + log_filename,
        'format': '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    }
    logging.basicConfig(**config_dict)


def config_redis(app):
    redis.init_app(app)


def config_session(app):
    session.init_app(app)


app = create_app()
