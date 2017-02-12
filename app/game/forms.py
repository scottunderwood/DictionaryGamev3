from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from wtforms import ValidationError

#make unique game forms for all of the various game logic prompts?
#attempt at making a game form    
class GameForm(Form):
    prompt = StringField('prompt', validators=[Required()])
    submit = SubmitField('Submit')