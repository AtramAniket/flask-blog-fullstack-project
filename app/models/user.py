from app.extensions import db
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):

	__tablename__ = "users"

	def __repr__(self):
		return f"User {self.username}"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	username: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
	email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
	password: Mapped[str] = mapped_column(String(100), nullable=False)
	role: Mapped[str] = mapped_column(String(100), nullable=False, default="user")

	def set_password(self, raw_password_text):

		self.password = generate_password_hash(raw_password_text, method="pbkdf2:sha256:600000", salt_length=8)

	def check_password(self, raw_password_text):

		return check_password_hash(self.password, raw_password_text)
