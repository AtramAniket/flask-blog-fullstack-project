from flask import Flask
from .routes.posts import posts_bp
from .extensions import db, bootstrap


def create_app():

	app = Flask(__name__)

	app.config.from_object('config.Config')

	app.register_blueprint(posts_bp)

	bootstrap.init_app(app)

	db.init_app(app)


	return app