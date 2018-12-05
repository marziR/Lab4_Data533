def net_annual_salary(hrsperweek,payperhr):
        gross=hrsperweek*payperhr*52
        if gross <50000:
            return (round(gross*0.7))
        elif gross>= 50000:
            return (round(gross*0.6))