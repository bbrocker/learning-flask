from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# message = "..." does NOT work for DataRequired validator, it always shows the message "Please fill out this field."
class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired(message="Please enter your first name.")])
    last_name = StringField('Last name', validators=[DataRequired(message="Please enter your last name.")])
    email = StringField('Email', validators=[DataRequired(), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Passwords must be 6 chars or more.")])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit = SubmitField('Sign in')
