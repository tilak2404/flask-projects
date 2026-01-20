from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name=StringField('Please enter the name of puppy')
    submit=SubmitField('Add puppy')
class DelForm(FlaskForm):
    id=IntegerField('Please enter the id of puppy')
    submit=SubmitField('Delete puppy')