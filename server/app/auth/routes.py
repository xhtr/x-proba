from app.auth import forms
from app.auth import bp
from flask import render_template
from flask import request, flash, redirect, url_for
from sxmodel.Users import User
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import login_user, current_user


@bp.route('/auth/register', methods = ['POST', 'GET'])
def register():
    title = 'Register Form'
    reg_form = forms.LoginForm()
    if request.method == 'POST' and reg_form.validate():
        new_user = User(login = reg_form.username.data,
                    password = generate_password_hash(reg_form.password.data)
                    )

        db.session.add(new_user)
        db.session.commit()

    return render_template('register.html', title = title, form = reg_form)


@bp.route('/auth/login', methods = ['POST', 'GET'])
def login():
    title = 'Login'
    login_form = forms.LoginForm()
    if request.method == 'POST' and login_form.validate():
        user = User.query.filter_by(login=login_form.username.data).first()

        if user is None or not check_password_hash(user.password, login_form.password.data):
            flash('User or Password Invalid')
            return redirect(url_for('auth.register'))

    flash('Successfully logged')
    return render_template('register.html', title = title, form = login_form)
