from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=30)])
    ingredients = StringField('Ingredients', validators=[DataRequired(), Length(min=2, max=30)])
    instructions = StringField('Instructions', validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired(), Length(min=2, max=30)])
    submit = SubmitField('Submit')
