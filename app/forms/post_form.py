from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, URL, Length
from flask_ckeditor import CKEditorField

class PostForm(FlaskForm):
	title = StringField("Title", validators=[DataRequired("Title is required")])
	subtitle = StringField("Subtitle", validators=[DataRequired("Subtitle is required")])
	body = CKEditorField("Blog Content", validators=[DataRequired("Blog content cannot be empty")])
	img_url = StringField("Image URL", validators=[DataRequired("Image URL is required"), URL("Must be a valid url")])
	submit = SubmitField()