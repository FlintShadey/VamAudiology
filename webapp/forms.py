from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    login_submit = SubmitField('Login')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"id": "signupPassword"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')],  render_kw={"id": "signupPasswordConfirm"})
    register_submit = SubmitField('Sign Up')

