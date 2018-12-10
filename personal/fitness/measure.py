def calc(weight, height):
    
    try:  
        BMI = int(float(weight) / float(height)**2)
   
    except ValueError:
        return('both entries must be numbers')
        
    except ZeroDivisionError: 
        return("Division by 0,height cant be zero!")     
        
    else:    
        return BMI
