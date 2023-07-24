from .models import *
from .daos import *
import datetime

class RentBusiness: 
    def calc_desconto(self, date, client_id, theme_id):
        client_rents = RentDao().clientRents(client_id) 
        price = ThemeDao().getTheme(theme_id).price
        day = date.weekday()
        if client_rents:
            if day in (1, 2, 3):
                price = price*0.6
            elif day in (4, 5):
                price = price*0.9
        return price