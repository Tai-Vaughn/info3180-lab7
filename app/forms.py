from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField('Biography', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])