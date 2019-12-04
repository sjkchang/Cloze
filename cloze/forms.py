"""
forms.py
====================================
File for all of the Custom FlaskForms we use
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    """
    A registration FlaskForm
    """
    username = StringField('Username', validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=8)])
    confirmPassword = PasswordField('Confirm Password', validators = [DataRequired(), Length(min=8), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """
        Determines if a username is already in use

        Parameters
        ----------
        username
            The username that is being checked
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already in use')

    def validate_email(self, email):
        """
        Determines if an email is already in use

        Parameters
        ----------
        username
            The email that is being checked
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    """
    A login FlaskForm
    """
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=8, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    """
    A update account FlaskForm
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class MealLogForm(FlaskForm):
    """
    A Meallog FlaskForm
    """
    food = StringField('Meal', validators=[DataRequired()])
    servings = IntegerField('Servings', validators=[DataRequired()])
    calories = IntegerField('Calories', validators=[DataRequired()])
    protein = IntegerField('Protein', validators=[DataRequired()])
    carb = IntegerField('Carbs', validators=[DataRequired()])
    fat = IntegerField('Fat', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ToDoForm(FlaskForm):
    """
    A to do list FlaskForm
    """
    entry = StringField('Entry')
    submit = SubmitField('Submit')

class ChallengeForm(FlaskForm):
    """
    A challenge FlaskForm
    """
    title = StringField('Challenge', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create')

class EntryForm(FlaskForm):
    """
    A journal entry FlaskForm
    """
    title = StringField('Challenge', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Add')
