# -*- coding: utf-8 -*-
from datetime import datetime
from uuid import uuid4

from app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    connected_at = db.Column(db.DateTime, default=datetime.utcnow)
    available = db.Column(db.Boolean, default=True)
    public_id = db.Column(db.String, default=str(uuid4()))

    profile = db.relationship('Profile', backref='user', lazy=True)
    contact = db.relationship('Contact', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.login


class Profile(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    firstname = db.Column(db.Unicode(64))
    lastname = db.Column(db.Unicode(64))
    sex = db.Column(db.String(20))
    birthdate = db.Column(db.Date)
    birthcity = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Contact(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True)
    phone_mobile = db.Column(db.String(20))
    phone_fix = db.Column(db.String(20))
    address = db.Column(db.Unicode(255))
    zipcode = db.Column(db.String(20))
    city = db.Column(db.Unicode(128))
    country = db.Column(db.Unicode(128))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
