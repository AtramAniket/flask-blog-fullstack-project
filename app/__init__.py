from flask import Flask
from .routes.posts import posts_bp
from .routes.users import users_bp
from .extensions import db, bootstrap, ckeditor


def create_app():

	app = Flask(__name__)

	app.config.from_object('config.Config')

	app.register_blueprint(posts_bp)

	app.register_blueprint(users_bp, url_prefix="/users")

	bootstrap.init_app(app)

	ckeditor.init_app(app)

	db.init_app(app)


	return app