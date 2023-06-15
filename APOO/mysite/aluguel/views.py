from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .daos import ItemDao

from .models import *

#Página inicial com a lista de clientes
def index(request):
    return render(request, 'index.html')

class ItemViews:
    #Recupera a lista de itens cadastrados
    def listItem(request):
        i = ItemDao()
        item_list = i.list_all
        context = {'item_list': item_list}
        return render(request, 'aluguel/listItem.html', context)
    
    #Redirecionador para o formulário de cadastro de item
    def formItem(request):
        return render(request, 'aluguel/formItem.html')

    #Salva o novo item e volta para listagem de itens
    def saveItem(request):
        i = ItemDao()
        i.save(request)
        return redirect('/listItem')

    #Deleta um item e volta para listagem de itens
    def deleteItem(request, id):
        i = ItemDao()
        i.delete(request, id)
        return redirect('/listItem')
    
    #Pega um item pelo ID e enviar para o form de edição
    def detailItem(request, id):
        i = ItemDao()
        item = i.detail(request, id)
        return render(request, 'aluguel/formEditItem.html', {'item': item} )

    #Atualiza um item e volta para listagem
    def updateItem(request, id):
        i = ItemDao()
        i.update(request, id)
        return redirect('/listItem')
