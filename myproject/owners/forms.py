from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name=StringField("Add the owner to the puppy")
    id=IntegerField('Enter the puppy id')
    submit=SubmitField('Add owner to puppy')