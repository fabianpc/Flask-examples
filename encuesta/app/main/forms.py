from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired


class SurveyForm(FlaskForm):
    unitName = StringField()
    researchDate = DateField()
    unitProvince = StringField(validators=[DataRequired()])
    unitCanton = StringField()
    unitParish = StringField()
    lastName = StringField()
    surName = StringField()
    firstName = StringField()
    middleName = StringField()
    sex = StringField()
    birthDate = DateField()
    ageYears = IntegerField()
    ageMonths = IntegerField()
    ageDays = IntegerField()
    civilState = StringField()
    educationLevel = StringField()
    occupation = StringField()
    telephone = StringField()
    residenceProvince = StringField()
    residenceCanton = StringField()
    residenceParish = StringField()
    address = StringField()
    liable = StringField()