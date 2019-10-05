from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2,max=10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = StringField('Sign up')


class LoginForms(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = StringField('Login')
