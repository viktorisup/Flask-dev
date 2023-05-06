from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField


class UserAuthForm(FlaskForm):
    email = StringField("E-mail", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    submit = SubmitField("Login")
