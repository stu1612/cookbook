from flask_wtf import Form
from wtforms import StringField

class Recipeform(Form):
    title = StringField('Title', validators=[])
    
    