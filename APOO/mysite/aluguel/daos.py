from .models import Item 

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
        