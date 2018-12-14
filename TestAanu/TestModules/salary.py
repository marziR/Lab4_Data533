def net_annual_salary(hrsperweek,payperhr):
    
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
