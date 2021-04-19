from flask_wft import FlaskForm
from flask_wft.file import FileField
from wtforms import SubmitField

class MyForm(FlaskForm):
    file = FileField('file')
    submit = SubmitField('submit')
