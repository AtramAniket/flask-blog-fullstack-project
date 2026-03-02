from app import create_app
from app.extensions import db
from app.models.post import Post

app = create_app()

with app.app_context():
	db.create_all()
	print("Database model created successfully.")