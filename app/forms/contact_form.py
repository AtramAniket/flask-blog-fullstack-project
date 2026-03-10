from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired("Name is required")])
    email = StringField("Email", validators=[DataRequired("Email address is required"), Email(message="Enter a valid email address")])
    message = TextAreaField("Message", validators=[DataRequired("Message is required")])
    submit = SubmitField("Send")