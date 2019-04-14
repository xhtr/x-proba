# -*- coding: utf-8 -*-
from flask import Flask
import config

from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from redis import StrictRedis
from werkzeug.contrib.fixers import ProxyFix


session = Session()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()
login_manager = LoginManager()
csrf = CSRFProtect()
talisman = Talisman()
db = SQLAlchemy()
migrate = Migrate()


def create_app(cfg=config):
    app = Flask(__name__)
    app.config.from_object(cfg)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    cfg = app.config
    csp = cfg['CSP']
    cache_redis = StrictRedis(
        host=cfg['REDIS_CACHE_HOSTNAME'],
        port=cfg['REDIS_CACHE_PORT'])

    cfg.update(CACHE_REDIS=cache_redis)
    cfg.update(SESSION_REDIS=cache_redis)

    session.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    babel.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    talisman.init_app(app, content_security_policy=csp)
    db.init_app(app)
    migrate.init_app(app, db)

    app.redis_cache = cache_redis

    from app.wide import bp as bp_wide
    from app.wide import filters
    from app.main import bp as bp_main
    from app.auth import bp as bp_auth

    app.register_blueprint(bp_wide)
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)

    app.jinja_env.filters['map_obj_true'] = filters.map_obj_true
    app.jinja_env.filters['str_3dots'] = filters.str_3dots
    app.jinja_env.filters['uppercase_first_letter'] = filters.uppercase_phrase
    app.jinja_env.filters['last_char_dot'] = filters.last_char_dot
    app.jinja_env.filters['format_timestamp'] = filters.format_timestamp
    app.jinja_env.filters['hide_string'] = filters.hide_string
    app.jinja_env.filters['first_word'] = filters.first_word
    app.jinja_env.filters['first_char'] = filters.first_char
    app.jinja_env.filters['to_date_humanize'] = filters.to_date_humanize
    app.jinja_env.globals['url_for_other_page'] = filters.url_for_other_page

    return app
