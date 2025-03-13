from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import User, Conference

main = Blueprint('main', __name__)

@main.route('/')
def home():
    conferences = Conference.query.all()
    return render_template('index.html', conferences=conferences)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        new_user = User(name=name, email=email, password=password, role="Attendee")
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html')
