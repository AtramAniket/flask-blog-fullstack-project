from flask import Flask
from .models.user import User
from .routes.posts import posts_bp
from .routes.users import users_bp
from .extensions import db, bootstrap, ckeditor, login_manager

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# @app.context_processor
# def inject_current_year():
#     return {'current_year': datetime.utcnow().year}

def create_app():

	app = Flask(__name__)

	app.config.from_object('config.Config')

	app.register_blueprint(posts_bp)

	app.register_blueprint(users_bp, url_prefix="/users")

	bootstrap.init_app(app)

	ckeditor.init_app(app)

	login_manager.init_app(app)

	login_manager.login_view = "users.login"

	login_manager.login_message_category = "danger"

	login_manager.login_message = "You must be logged in to access this page"

	db.init_app(app)

	return app