# -*- coding: utf-8 -*-
from app.main import bp


@bp.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@bp.route('/frequencies', methods=['GET'])
def frequencies():
    return '0'
