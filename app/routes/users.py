from app.extensions import db
from app.models.user import User
from sqlalchemy.exc import IntegrityError
from app.forms.login_form import LoginForm
from app.forms.registration_form import RegistrationForm
from flask_login import login_user, logout_user, current_user, login_required
from flask import Blueprint, render_template, url_for, redirect, request, flash

users_bp = Blueprint('users', __name__)

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
	
	form = LoginForm()

	if request.method == 'POST':
		
		if form.validate_on_submit():

			email = form.email.data

			password = form.password.data

			user = User.query.filter_by(email=email).first()

			if user and user.check_password(password):
				login_user(user)
				flash(f"Welcome back {email}", "success")
				return redirect(url_for("posts.home"))
			else:
				flash(f"User not found", "danger")
				return redirect(url_for("users.login"))

			print(email)
			print(password)

	return render_template('login.html', form=form)

@users_bp.route('/logout')
@login_required
def logout():
	logout_user()
	flash("You have been logged out", "info")
	return redirect(url_for("users.login"))

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()

	if request.method == 'POST':
		
		if form.validate_on_submit():
			
			user_name = form.username.data

			email = form.email.data

			password = form.password.data

			confirm_password = form.confirm_password.data

			# Add new user to DB
			new_user = User(username=user_name, email=email)
			
			new_user.set_password(password)

			db.session.add(new_user)
			try:
				db.session.commit()
			except IntegrityError:
				db.session.rollback()
				flash("Unexpected DB error", "danger")
				return redirect(url_for('users.register'))
			else:
				flash("Account created successfully", "success")
				return redirect(url_for('users.login'))

	return render_template('register.html', form=form)
