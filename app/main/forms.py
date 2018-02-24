from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class NameForm(Form):
    name = StringField('what is your name?', validators=[InputRequired()])
    submit = SubmitField('Submit')