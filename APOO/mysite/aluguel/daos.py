from .models import *
from .business import *

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

    def clientRents(self, client_id):
        return Rent.client_set.filter(id = client_id)

    def saveRent(self, date, start_hours, end_hours, client_id, theme_id, price, street, number, complement, district, city, state):
        r = Rent()
        r.date=date
        r.start_hours=date
        r.end_hours=date
        r.price=price
        r.client_id=client_id
        r.theme_id=theme_id
        r.street = street,
        r.number = number,
        r.complement = complement,
        r.district = district, 
        r.city = city,
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
        r.street = street,
        r.number = number,
        r.complement = complement,
        r.district = district, 
        r.city = city,
        r.state = state

        r.save()
    
