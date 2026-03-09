from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Email address is required"), Email(message="Enter a valid email address")])
    password = PasswordField("Password", validators=[DataRequired("Password is required")])
    submit = SubmitField("Login")