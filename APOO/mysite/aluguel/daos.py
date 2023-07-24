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

class AdressDao:
    def list_all(self):
        return Address.objects.all()