from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

bootstrap = Bootstrap5()

ckeditor = CKEditor()

login_manager = LoginManager()

migrate = Migrate()
