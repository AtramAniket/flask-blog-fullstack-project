from app.extensions import db
from app.models.user import User
from sqlalchemy.exc import IntegrityError
from app.forms.login_form import LoginForm
from app.forms.registration_form import RegistrationForm
from flask_login import login_user, logout_user, current_user, login_required
from flask import Blueprint, render_template, url_for, redirect, request, flash, abort

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
				login_user(new_user)
				flash(f"Welcome {new_user.username}", "success")
				return redirect(url_for('posts.home'))
			except IntegrityError:
				db.session.rollback()
				flash("Unexpected DB error", "danger")
				return redirect(url_for('users.register'))
			else:
				flash("Account created successfully", "success")
				return redirect(url_for('users.login'))

	return render_template('register.html', form=form)

@users_bp.route('/show')
@login_required
def show_users():
    if current_user.role != "admin":
        return render_template('404.html')

    # Only show users with role "user"
    users = User.query.filter_by(role="user").order_by(User.username.asc()).all()
    return render_template("users.html", users=users)


@users_bp.route('/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role != "admin":
        return render_template('404.html')

    user = User.query.get_or_404(user_id)
    
    if user.role != "user":  # prevent admin deletion
        return render_template('404.html')

    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users.show_users'))