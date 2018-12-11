
# coding: utf-8
# In[1]:
#classify.py
def bmicat(BMI):
    try:
        if BMI == 0:
            raise ValueError
        if type(BMI) == str:
            raise TypeError
        elif (BMI > 0 and BMI < 18.5):
            return 'Underweight'
        elif (BMI >= 18.5 and BMI <= 24.9):
            return 'Healthy'
        elif (BMI >= 25 and BMI <30):
            return 'Overweight'
        elif (BMI >= 30 and BMI < 35):
            return 'Obese'
        elif (BMI >= 35):
            return 'Morbidly Obese'
    except ValueError:
        print('Invalid BMI')
    except TypeError:
        print('Invalid Data Type')
