
# coding: utf-8
# In[3]:
#measure.py
def calc(weight, height):
    try:
        BMI = float((weight) / (height * height))
        if weight <= 0:
            raise ValueError
        if height > 3:
            raise ValueError
        if height <= 0:
            raise ZeroDivisionError
        else:
            return (round(BMI,1))
    except ValueError:
        print("Value invalid!")
    except ZeroDivisionError:
        print('Cannot divide by 0')
