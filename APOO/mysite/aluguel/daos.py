from .models import *

class ClientDao:    
    def list_all(self):
        return Client.objects.all()

class PhoneDao:
    def new_phone(ddd, number, client):
        return Phone(ddd=ddd, number=number, client=client)

class ThemeDao:
    def list_all(self):
        return Theme.objects.all()

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
        client_list = ClientDao().list_all() #Client.objects.all()
        theme_list = ThemeDao().list_all() #Theme.objects.all()
        return {'client_list':client_list, 'theme_list': theme_list}

    def deleteRent(self, id):
        r = Rent.objects.get(pk=id)
        r.delete()

    def getRent(self, id):
        return Rent.objects.get(pk=id)

    def saveRent(date, start_hours, end_hours, price, client_id, theme_id, address):
        r = Rent(date, start_hours, end_hours, price, client_id, theme_id, address)
        r.save()

    

class AdressDao:
    def new_address(street, number, complement, district, city, state):
        return Address(street, number, complement, district, city, state)