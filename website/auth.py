from flask import Blueprint, render_template, request, redirect, url_for
from .models import Candidates
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password = request.form.get('password')

        candidate = Candidates.query.filter_by(email=email).first()

        if candidate:
            if check_password_hash(candidate.password,password):
                print('Logged in')
                login_user(candidate, remember=True)
                return redirect(url_for('views.home'))
            else:
                print('Incorrect password')
        else:
            print('Email does nor exist')
    return render_template("login.html", candidate=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email = request.form.get('email')
        password=request.form.get('password')
        name=request.form.get('name')
        identity_number=request.form.get('identity_number')
        date_of_birth=request.form.get('date_of_birth')

        candidate = Candidates.query.filter_by(email=email).first()
        if candidate:
            print('Email already exist')
            return redirect(url_for('views.home'))

        new_candidate=Candidates(email=email,name=name,password=generate_password_hash(password, method='sha256'),identity_number=identity_number,date_of_birth=date_of_birth)
        db.session.add(new_candidate)
        db.session.commit()
        login_user(new_candidate, remember=True)

        return redirect(url_for('views.home'))

    return render_template("sign_up.html", candidate=current_user)





