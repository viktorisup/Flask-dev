from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserRegisterForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    email = StringField("E-mail", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message='Field must be equal to password')
    ])
    confirm_password = PasswordField("Confirm password", [validators.DataRequired()])
    submit = SubmitField("Register")
