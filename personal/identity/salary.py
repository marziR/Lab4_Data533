def net_annual_salary(hrsperweek,payperhr):
    try:
        gross=hrsperweek*payperhr*52
        if payperhr < 11.50:
            raise ValueError
        if type(hrsperweek) == str:
            raise TypeError
        if type(payperhr) == str:
            raise TypeError
        if gross <50000:
            return (round(gross*0.7))
        elif gross>= 50000:
            return (round(gross*0.6))

    except ValueError:
        print('Below minimum wage!')
    except TypeError:
        print('Invalid Data Type')
