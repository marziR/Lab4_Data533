def calc(weight, height):
<<<<<<< HEAD
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
=======
    
    try:  
        BMI = int(float(weight) / float(height)**2)
   
    except ValueError:
        return('both entries must be numbers')
        
    except ZeroDivisionError: 
        return("Division by 0,height cant be zero!")     
        
    else:    
        return BMI
>>>>>>> origin
