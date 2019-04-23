# -*- coding: utf-8 -*-
from app.main import bp
from flask import render_template

@bp.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@bp.route('/', methods=['GET'])
def landing():
    return '0'

from os import listdir

@bp.route('/frequencies', methods=['GET'])
def frequencies():
    title = 'Frecuencies 1 & 2 '
    with open('app/main/frequencies.txt') as f:
        lines = f.read()

    frec_seen = []
    x = 0
    rep_frec = []
    i = 0
    while i < 2:
        for line in lines.splitlines():
            x = x + int(line)
            if x in frec_seen:
                rep_frec.append(x)

            frec_seen.append(x)
        i += 1
    if len(rep_frec) != 0:
        rep_frec = rep_frec[0]
    else:
        rep_frec = 'None'



    return render_template('ini.html', fr=x/2, rep=rep_frec, title=title)

