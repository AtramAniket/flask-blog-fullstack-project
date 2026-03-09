from datetime import datetime
from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, func, Text

class Post(db.Model):

	__tablename__ = "blog_posts"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	title: Mapped[str] = mapped_column(String(255),nullable=False)
	subtitle: Mapped[str] = mapped_column(String(255), nullable=False)
	body: Mapped[str] = mapped_column(Text, nullable=False)
	author: Mapped[str] = mapped_column(String(255), nullable=False)
	img_url: Mapped[str] = mapped_column(String(255), nullable=False)
	created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
	updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())