from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap5()
ckeditor = CKEditor()
login_manager = LoginManager()