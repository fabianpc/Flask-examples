import datetime as dt


def calculateAge(strBirthDate):
    currentDate = dt.datetime.now()
    birthDate = dt.datetime.strptime(strBirthDate, '%Y-%m-%d')
    daysLeft = currentDate - birthDate
    years = ((daysLeft.total_seconds()) / (365.242 * 24 * 3600))
    yearsInt = int(years)
    months = (years - yearsInt) * 12
    monthsInt = int(months)
    days = (months - monthsInt) * (365.242 / 12)
    daysInt = int(days)
    return [yearsInt, monthsInt, daysInt]
