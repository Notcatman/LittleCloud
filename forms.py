from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    name = StringField(' ', validators=[DataRequired()])
    submit = SubmitField('Add Text')

