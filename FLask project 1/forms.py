from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name=StringField('Please enter the name of puppy')
    submit=SubmitField('Add puppy')
class DelForm(FlaskForm):
    id=IntegerField('Please enter the id of puppy')
    submit=SubmitField('Delete puppy')
class AddOwner(FlaskForm):
    name=StringField("Add the owner to the puppy")
    id=IntegerField('Enter the puppy id')
    submit=SubmitField('Add owner to puppy')
