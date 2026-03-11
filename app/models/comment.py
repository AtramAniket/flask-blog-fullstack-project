from datetime import datetime
from app.extensions import db
from sqlalchemy import Integer, DateTime, func, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Comment(db.Model):

	__tablename__ = "comments"

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	text: Mapped[str] = mapped_column(Text, nullable=False)
	created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

	user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

	post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"), nullable=False, index=True)

	author: Mapped["User"] = relationship(back_populates="comments")

	post: Mapped["Post"] = relationship(back_populates="comments")