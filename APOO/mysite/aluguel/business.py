from .models import *
from .daos import *
from datetime import datetime

def calc_desconto(date, client_id, theme_id):
    client_rents = clientRents(client_id)
    #client_rents = [] 
    price = ThemeDao().getTheme(theme_id).price
    #price = 3000.00
    day = datetime.strptime(date, '%Y-%m-%d').weekday()
    if client_rents:
        if day in (1, 2, 3):
            price = price*0.6
        elif day in (4, 5):
            price = price*0.9
    return price