# -*- coding: utf-8 -*-
from flask import Blueprint


bp = Blueprint('wide', __name__)


from app.wide import routes
