from flask import render_template, request
from . import main
from .forms import SurveyForm
from ..models.survey import Survey
from app import db
import sys


@main.route('/')
def index():
    form = SurveyForm()
    return render_template('index.html', form=form)


@main.route('/', methods=['POST'])
def survey_save():
    survey = Survey()
    survey.unitName = request.form["unitName"]
    survey.researchDate = request.form["researchDate"]
    survey.unitProvince = request.form["unitProvince"]
    survey.unitCanton = request.form["unitCanton"]
    survey.unitParish = request.form["unitParish"]
    survey.lastName = request.form["lastName"]
    survey.surName = request.form["surName"]
    survey.firstName = request.form["firstName"]
    survey.middleName = request.form["middleName"]
    survey.sex = request.form["sex"]
    survey.birthDate = request.form["birthDate"]
    survey.ageYears = request.form["ageYears"]
    survey.ageMonths = request.form["ageMonths"]
    survey.ageDays = request.form["ageDays"]
    survey.civilState = request.form["civilState"]
    survey.educationLevel = request.form["educationLevel"]
    survey.occupation = request.form["occupation"]
    survey.telephone = request.form["telephone"]
    survey.residenceProvince = request.form["residenceProvince"]
    survey.residenceCanton = request.form["residenceCanton"]
    survey.residenceParish = request.form["residenceParish"]
    survey.address = request.form["address"]
    survey.liable = request.form["liable"]
    try:
        db.session.add(survey)
        db.session.commit()
        return 'Datos correctamente registrados!'
    except:
        print('Se produjo error', sys.exc_info()[1])
        return 'Error!'