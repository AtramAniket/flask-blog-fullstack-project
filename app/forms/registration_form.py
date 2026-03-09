from flask_wtf import FlaskForm
from app.models.user import User
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired("Username is required")])
    email = StringField("Email", validators=[DataRequired("Email is required"), Email(message="Enter a valid email address")])
    password = PasswordField("Password", validators=[DataRequired("Password is required")])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired("Please re-enter password"), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_email(self, email):

        if User.query.filter_by(email=email.data).first():
            
            raise ValidationError("Email address already in use")

    def validate_username(self, username):

        if User.query.filter_by(username=username.data).first():
            
            raise ValidationError("Username already taken")
