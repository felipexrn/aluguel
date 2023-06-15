from .models import Item 

class ItemDao:
    def list_all(self):
        return Item.objects.all()

    def save(self, request):
        i = Item(name=request.POST['name'], 
                 description=request.POST['description'])
        i.save()

    def delete(self, request, id):
        i = Item.objects.get(pk=id)
        i.delete()

    def detail(self, request, id):
        return Item.objects.get(pk=id)

    def update(self, request, id):
        i = Item.objects.get(pk=id)
        i.name = request.POST['name']
        i.description = request.POST['description']
        i.save()
        