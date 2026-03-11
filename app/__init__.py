from datetime import datetime
from .models.user import User
from .models.post import Post
from .routes.posts import posts_bp
from .routes.users import users_bp
from .models.comment import Comment
from flask import Flask, render_template
from .extensions import db, bootstrap, ckeditor, login_manager, migrate

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

def create_app():

	app = Flask(__name__)

	app.config.from_object('config.Config')

	app.register_blueprint(posts_bp)

	app.register_blueprint(users_bp, url_prefix="/users")

	db.init_app(app)

	ckeditor.init_app(app)

	bootstrap.init_app(app)

	from app import models

	migrate.init_app(app, db)

	login_manager.init_app(app)

	login_manager.login_view = "users.login"

	login_manager.login_message_category = "danger"

	login_manager.login_message = "You must be logged in to access this page"

	# Register error handlers
	@app.errorhandler(404)
	def page_not_found(e):
		return render_template("404.html"), 404

	# dynamically display current year in footer
	@app.context_processor
	def inject_current_year():
		return {'current_year': datetime.utcnow().year}

	return app