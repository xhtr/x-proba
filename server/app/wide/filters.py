# -*- coding: utf-8 -*-
from flask import g
from flask import request
from flask import url_for
from datetime import datetime
import arrow


def map_obj_true(a):
    return {k: True for k in [k for k, v in a.iteritems() if v]}


def str_3dots(s, _max=29):
    __MAX_S__ = _max
    return s.replace(s[__MAX_S__:], ' ...') if len(s) > __MAX_S__ else s


def uppercase_phrase(s):
    first = s[0] if len(s) > 0 else ''
    remaining = s[1:] if len(s) > 1 else ''
    return first.upper() + remaining


def last_char_dot(s):
    s = s.strip()
    last = s[-1] if len(s) > 0 else ''
    if last == '.':
        return s
    return s + '.'


def format_timestamp(d, format_=None, locale=True):
    date = datetime.utcfromtimestamp(d)
    if format_ is None:
        if g.locale == 'es':
            return format_datetime(date, format='dd/MM/yyyy', rebase=locale)
        else:
            return format_datetime(date, format='MM/dd/yyyy', rebase=locale)
    return format_datetime(date, format=format_, rebase=locale)


def hide_string(s):
    s = list(s.strip())
    for i, c in enumerate(s[:-1]):
        s[i] = '*'
    return ' '.join(s)


def first_word(s):
    if not s:
        return ''
    s = s.split(' ')
    return s[0] if len(s) > 0 else ''


def first_char(s):
    if not s:
        return ''
    return '%s.' % s[0] if len(s) > 0 else ''


def url_for_other_page(page):
    args = request.args.copy()
    args['pageStart'] = page
    return url_for(request.endpoint, **args)


def to_date_humanize(ts):
    return arrow.get(ts).humanize()
