<<<<<<< HEAD
def bmicat(BMI):
    try:
        if (BMI > 0 and BMI < 18.5):
            return 'Underweight'
        elif (BMI >= 18.5 and BMI <= 24.9):
            return 'Healthy'
        elif (BMI >= 25 and BMI <30):
            return 'Overweight'
        elif (BMI >= 30 and BMI < 35):
            return 'Obese'
        elif (BMI >= 35):
            return 'Morbidly Obese'
        elif (BMI == 0):
            raise ValueError
    except ValueError:
        return 'Invalid BMI'
    except TypeError:
        return 'Invalid Data Type'
=======

def bmicat(BMI):

    if (BMI < 18.5):
        return 'Underweight'

    elif (BMI >= 18.5 and BMI <= 24.9):
        return 'Healthy'

    elif (BMI >= 25 and BMI <30):
        return 'Overweight'

    elif (BMI >= 30 and BMI < 35):
        return 'Obese'
    else:
        (BMI >= 35)
        return 'Morbidly Obese'
>>>>>>> origin
