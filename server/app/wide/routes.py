# -*- coding: utf-8 -*-
from flask import current_app
from flask import has_request_context
from flask import request
from flask import session as fsession
from app import babel

from app.wide import bp


@babel.localeselector
def get_locale():
    langs_available = current_app.config['LANGUAGES']

    if has_request_context():
        # Return lang from browser with request context
        browser = request.accept_languages.best_match(langs_available)
        find_lng = False
        for l in langs_available:
            if browser == l:
                find_lng = True
                break
        if find_lng is False:
            browser = current_app.config['BABEL_DEFAULT_LOCALE']
        return fsession.get('lang', browser)

    # mainly use for test purpose
    with current_app.test_request_context():
        browser = request.accept_languages.best_match(langs_available)
        find_lng = False
        for l in langs_available:
            if browser == l:
                find_lng = True
                break
        if find_lng is False:
            browser = current_app.config['BABEL_DEFAULT_LOCALE']
        return fsession.get('lang', browser)


@babel.timezoneselector
def get_timezone():
    if has_request_context():
        tz = fsession.get('tz', None)
        return tz

    # mainly use for test purpose
    with current_app.test_request_context():
        tz = fsession.get('tz', None)
        return tz
