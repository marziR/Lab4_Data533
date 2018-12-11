from datetime import  datetime

def calculate_age(DOB):
    try:
        currentyear= datetime.today().year
        currentmonth= datetime.today().month
        currentday= datetime.today().day
        bornyear=int(DOB[0:4])
        bornmonth=int(DOB[5:7])
        bornday=int(DOB[8:10])

        if bornyear > currentyear:
            raise ValueError
        if bornmonth > 12:
            raise ValueError
        else:
            age=(currentyear - bornyear - ((currentmonth, currentday) < (bornmonth, bornday)))
            return age

    except ValueError:
        print('Invalid Date!')

    
