# -*- coding: utf-8 -*-
from flask import current_app
from flask import make_response
from flask import redirect
from flask import request
from flask import url_for
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature
from itsdangerous import SignatureExpired
from app import login_manager


# Uses Facebook like default expiration for token
# token that can be used for API
EXPIRE_FB_DEFAULT_60 = 60 * 1 * 60 * 24 * 61


class User(UserMixin):
    token_id = None  # for auth api for example.
    role = None
    level = '0001'

    def generate_auth_token(self, expiration=EXPIRE_FB_DEFAULT_60):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'token_id': str(self.token_id)})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            # valid token, but expired
            return None
        except BadSignature:
            # invalid token
            return None
        # TODO load user from db wiht .get(data['token_id'])
        return None


@login_manager.user_loader
def user_loader(user_id):
    # TODO load user from db
    return None


@login_manager.unauthorized_handler
def unauthorized():
    if request.accept_mimetypes['application/json'] >= \
            request.accept_mimetypes['text/html']:
        return make_response('Unauthorized', 401)
    return redirect(url_for('auth.login'))
