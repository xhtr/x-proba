# -*- coding:utf-8 -*-

worker_connections = 1001
workers = 2
reload = True
bind = "0.0.0.0:8077"
worker_class = "gevent"
pidfile = "/tmp/app.pid"
