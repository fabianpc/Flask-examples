from .. import db


class Survey(db.Model):
    __tablename__ = 'survey'
    unitName = db.Column(db.String(100), primary_key=True)
    researchDate = db.Column(db.Date(), primary_key=True)
    unitProvinceCode = db.Column(db.String(6))
    unitCantonCode = db.Column(db.String(6))
    unitParishCode = db.Column(db.String(6))
    lastName = db.Column(db.String(100))
    surName = db.Column(db.String(100))
    firstName = db.Column(db.String(100))
    middleName = db.Column(db.String(100))
    sex = db.Column(db.String(1))
    birthDate = db.Column(db.Date())
    ageYears = db.Column(db.Integer())
    ageMonths = db.Column(db.Integer())
    ageDays = db.Column(db.Integer())
    civilState = db.Column(db.String(2))
    educationLevel = db.Column(db.String(3))
    occupation = db.Column(db.String(100))
    telephone = db.Column(db.String(25))
    residenceProvince = db.Column(db.String(100))
    residenceCanton = db.Column(db.String(100))
    residenceParish = db.Column(db.String(100))
    address = db.Column(db.String(100))
    liable = db.Column(db.String(100))