from datetime import  datetime

def calculate_age(DOB):  
    
    class Error(Exception):
       """Base class for other exceptions"""
       pass

    class NotCorrectLengthEntry(Error):
       """Raised when the entry length is not correct"""
       pass

    class InvalidMonthEntry(Error):
       """Raised when month entry is larger that 12"""
       pass

    class InvalidDayEntry(Error):
       """Raised when the day entry is larger than 31"""
       pass
    
    try:
    
        if len(DOB) != 10:
            raise NotCorrectLengthEntry
        
        if  int(DOB[5:7]) > 12:
            raise InvalidMonthEntry
            
        if  int(DOB[8:10]) > 31:
            raise InvalidDayEntry    
        
    except NotCorrectLengthEntry:
        return('DOB must be a string of this format: YYYY-MM-DD')
    
    except InvalidMonthEntry:
        return("Month number cant be larger than 12")
        
    except InvalidDayEntry: 
        return("Day number cant be larger than 31")
        
    else:
        currentyear= datetime.today().year
        currentmonth= datetime.today().month
        currentday= datetime.today().day
        bornyear=int(DOB[0:4])
        bornmonth=int(DOB[5:7])
        bornday=int(DOB[8:10])
        age=(currentyear - bornyear - ((currentmonth, currentday) < (bornmonth, bornday)))
        return age
    