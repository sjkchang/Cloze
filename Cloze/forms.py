from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=8)])
    confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(), Length(min=8), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PlannerForm(FlaskForm):
    six = StringField('6:00')
    six30 = StringField('6:30')
    seven = StringField('7:00')
    seven30 = StringField('7:30')
    eight = StringField('8:00')
    eight30 = StringField('8:30')
    nine = StringField('9:00')
    nine30 = StringField('9:30')
    ten = StringField('10:00')
    ten30 = StringField('10:30')
    eleven = StringField('11:00')
    eleven30 = StringField('11:30')
    twelve = StringField('12:00')
    twelve30 = StringField('12:30')
    thirteen = StringField('13:00')
    thirteen30 = StringField('13:30')
    fourteen = StringField('14:00')
    fourteen30 = StringField('14:30')
    fifteen = StringField('15:00')
    fifteen30 = StringField('15:30')
    sixteen = StringField('16:00')
    sixteen30 = StringField('16:30')
    seventeen = StringField('17:00')
    seventeen30 = StringField('17:30')
    eighteen = StringField('18:00')
    eighteen30 = StringField('16:30')
    nineteen = StringField('19:00')
    nineteen30 = StringField('19:30')
    twenty = StringField('20:00')
    twenty30 = StringField('20:30')
    twentyone = StringField('21:00')
    twentyone30 = StringField('21:30')
    twentytwo = StringField('22:00')
    twentytwo30 = StringField('22:30')
    twentythree = StringField('23:00')
    twentythree30 = StringField('23:30')






    save = SubmitField('Save')
