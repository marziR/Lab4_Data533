def net_annual_salary(hrsperweek,payperhr):
<<<<<<< HEAD
    try:
        gross=hrsperweek*payperhr*52
        if payperhr < 11.50:
            raise ValueError
        if gross <50000:
            return (round(gross*0.7))
        elif gross>= 50000:
            return (round(gross*0.6))

    except ValueError:
        return 'Below minimum wage!'
    except TypeError:
        return 'Invalid Data Type'
=======
    
    class Error(Exception):
       """Base class for other exceptions"""
       pass

    class NotCorrectHrsPerWeek(Error):
       """Raised when the hours per week entry is not correct"""
       pass
    
    try:
        gross=int(hrsperweek)*int(payperhr)*52
        if hrsperweek > 168:
            raise NotCorrectHrsPerWeek
    
    except ValueError: 
        return("both entries should be integer types")     
            
    except NotCorrectHrsPerWeek:
        return("a week has only 168 hrs!")
   
    else:    
        
        if gross <50000:
            return (round(gross*0.7))
        elif gross>= 50000:
            return (round(gross*0.6))
>>>>>>> origin
