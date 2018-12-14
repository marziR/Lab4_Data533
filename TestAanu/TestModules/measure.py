def calc(weight, height):

    try:
        BMI = float((weight) / (height * height))
        if weight <= 0:
            raise ValueError
        elif height > 3:
            raise ValueError
        elif height <= 0:
            raise ZeroDivisionError
    except ValueError:
        return 'Value invalid!'
    except ZeroDivisionError:
        return 'Cannot divide by 0'
    else:
        return (round(BMI,1))
