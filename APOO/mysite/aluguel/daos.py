from .models import *
from datetime import datetime

class ClientDao:    
    def list_all(self):
        return Client.objects.all()

class PhoneDao:
    def new_phone(self, ddd, number, client):
        return Phone(ddd=ddd, number=number, client=client)

class ThemeDao:
    def list_all(self):
        return Theme.objects.all()
    
    def getTheme(self, id):
        return Theme.objects.get(pk=id)

class ItemDao:
    def list_all(self):
        return Item.objects.all()

    def save(self, n, d):
        i = Item(name = n, description = d)
        i.save()

    def delete(self, id):
        i = Item.objects.get(pk=id)
        i.delete()

    def detail(self, id):
        return Item.objects.get(pk=id)

    def update(self, n, d, id):
        i = Item.objects.get(pk=id)
        i.name = n 
        i.description = d
        i.save()
        
class RentDao:
    def list_all(self):
        return Rent.objects.all()

    def formRent(self):
        client_list = ClientDao().list_all()
        theme_list = ThemeDao().list_all()
        return {'client_list':client_list, 'theme_list': theme_list}

    def saveRent(self, date, start_hours, end_hours, client_id, theme_id, price, street, number, complement, district, city, state):
        r = Rent()
        r.date=date
        r.start_hours=date
        r.end_hours=date
        r.price=price
        r.client_id=client_id
        r.theme_id=theme_id
        r.street = street
        r.number = number
        r.complement = complement
        r.district = district
        r.city = city
        r.state = state
        r.save()

    def deleteRent(self, id):
        r = Rent.objects.get(pk=id)
        r.delete()

    def getRent(self, id):
        return Rent.objects.get(pk=id)

    def updateRent(self, id, date, start_hours, end_hours, client_id, theme_id, price, street, number, complement, district, city, state):
        r = Rent.objects.get(pk=id)
        r.date=date
        r.start_hours=date
        r.end_hours=date
        r.price=price
        r.client_id=client_id
        r.theme_id=theme_id
        r.street = street
        r.number = number
        r.complement = complement
        r.district = district
        r.city = city
        r.state = state

        r.save()

    def calc_desconto(self, date, client_id, theme_id):
        client_rents = RentDao().clientRents(client_id)
        price = ThemeDao().getTheme(theme_id).price
        day = datetime.strptime(date, '%Y-%m-%d').weekday()
        if client_rents:
            if day in (1, 2, 3):
                price = price*0.6
            elif day in (4, 5):
                price = price*0.9
        return price

    def clientRents(self, client_id):
        return Rent.objects.filter(client = client_id)
