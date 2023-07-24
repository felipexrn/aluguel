from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .daos import *
from .models import *
from .business import *

#Página inicial com a lista de clientes
def index(request):
    return render(request, 'index.html')


### ### ### ### ### ## VIEWS PARA CDU CLIENTE ## ### ### ### ### ###
class ClientViews:
    # Apresenta a lista de clientes no template listClient.html
    def listClient(request):
        clients_list = ClientDao().list_all() #Client.objects.all()
        context = {'clients_list': clients_list}
        return render(request, 'client/listClient.html', context)

    #Redirecionador para o formulário de cadastro
    def formClient(request):
        return render(request, 'client/formClient.html')

    #Salva o novo cliente e volta para listagem de clientes
    def saveClient(request):
        c = Client(name=request.POST['name'],
                   email=request.POST['email'])
        c.save()
        
        if(request.POST['ddd1']!=''):
            t1 = Phone(ddd=request.POST['ddd1'],
                   number=request.POST['phone1'],
                   client=c)
            t1.save()
            
        if(request.POST['ddd2']!=''):
            t2 = Phone(ddd=request.POST['ddd2'],
                   number=request.POST['phone2'],
                   client=c)
            t2.save()
            
        
        return redirect('/listClient')

    #Deleta um cliente e volta para listagem de clientes
    def deleteClient(request, id):
        c = Client.objects.get(pk=id)
        c.delete()
        return redirect('/listClient')

    #Pega um cliente pelo ID e enviar para o form de edição
    def detailClient(request, id):
        client = Client.objects.get(pk=id)
        return render(request, 'client/formEditClient.html', {'client': client} )

    #Atualiza um cliente e volta para listagem
    def updateClient(request, id):
        c = Client.objects.get(pk=id)
        c.name = request.POST['name']
        c.email = request.POST['email']
        c.save()
        #phones = Phone.objects.filter(client = c)
        if(request.POST['ddd1']!='' and request.POST['phone1']!='' ):
            if(c.phones.first()):
                t1 = c.phones.first()
                t1.ddd = request.POST['ddd1']
                t1.number = request.POST['phone1']
                t1.save()
            else: 
                t1 = Phone(ddd=request.POST['ddd1'],
                number=request.POST['phone1'],
                client=c)
                t1.save()
                      
        if(request.POST['ddd2']!='' and request.POST['phone2']!=''):
            if(c.phones.last() and c.phones.count()>1):
                t2 = c.phones.last()
                t2.ddd = request.POST['ddd2']
                t2.number =request.POST['phone2']
                t2.save()
            else: 
                t2 = Phone(ddd=request.POST['ddd2'],
                number=request.POST['phone2'],
                client=c)
                t2.save()    
            
        return redirect('/listClient')

### ### ### ### ### ## VIEWS PARA CDU TEMAS ## ### ### ### ### ###
class ThemeViews:
    #Recupera a lista de temas cadastrados
    def listTheme(request):
        themes_list = ThemeDao().list_all() #Theme.objects.all()
        context = {'theme_list': themes_list}
        return render(request, 'theme/listTheme.html', context)

    #Redirecionador para o formulário de cadastro de temas com itens existentes
    def formTheme(request):
        list_item = Item.objects.all()
        return render(request, 'theme/formTheme.html', {'list_item':list_item})

    #Salva o novo tema e volta para listagem de temas
    def saveTheme(request):
        t = Theme(name=request.POST['name'], 
                    color=request.POST['color'], 
                    price=request.POST['price'],
                    )
        t.save()
        my_list = request.POST.getlist('item')

        for i in my_list:
            item = Item.objects.get(id=i)
            t.itens.add(item)
        t.save()
        return redirect('/listTheme')
    
    #Deleta um tema e volta para listagem de temas
    def deleteTheme(request, id):
        t = Theme.objects.get(pk=id)
        t.delete()
        return redirect('/listTheme')

    #Pega um tema pelo ID e enviar para o form de edição
    def detailTheme(request, id):
        theme = Theme.objects.get(pk=id)
        return render(request, 'theme/formEditTheme.html', {'theme': theme} )

    #Atualiza um tema e volta para listagem
    def updateTheme(request, id):
        t = Theme.objects.get(pk=id)
        t.name = request.POST['name']
        t.color = request.POST['color']
        t.price = request.POST['price']
        t.save()
        return redirect('/listTheme')

### ### ### ### ### ## VIEWS PARA CDU ITEM ## ### ### ### ### ###

class ItemViews:
    #Recupera a lista de itens cadastrados
    def listItem(request):
        i = ItemDao()
        item_list = i.list_all
        context = {'item_list': item_list}
        return render(request, 'item/listItem.html', context)
    
    #Redirecionador para o formulário de cadastro de item
    def formItem(request):
        return render(request, 'item/formItem.html')

    #Salva o novo item e volta para listagem de itens
    def saveItem(request):
        n=request.POST['name'] 
        d=request.POST['description']
        i = ItemDao()
        i.save(n, d)
        return redirect('/listItem')

    #Deleta um item e volta para listagem de itens
    def deleteItem(request, id):
        i = ItemDao()
        i.delete(id)
        return redirect('/listItem')
    
    #Pega um item pelo ID e enviar para o form de edição
    def detailItem(request, id):
        i = ItemDao()
        item = i.detail(id)
        return render(request, 'item/formEditItem.html', {'item': item} )

    #Atualiza um item e volta para listagem
    def updateItem(request, id):
        i = ItemDao()
        n = request.POST['name']
        d = request.POST['description']
        i.update(n, d, id)
        return redirect('/listItem')

### ### ### ### ### ## VIEWS PARA CDU ALUGUEIS ## ### ### ### ### ###
class RentViews:
    
    #Recupera a lista de aluguéis cadastrados
    def listRent(request):
        rent_list = RentDao().list_all()
        context = {'rent_list': rent_list}
        return render(request, 'rent/listRent.html', context) 
    
    #Redirecionador para o formulário de cadastro de aluguel
    def formRent(request):
        context = RentDao().formRent()
        return render(request, 'rent/formRent.html', context)
    
    #Salva o novo aluguel e volta para listagem de alugueis
    def saveRent(request):
        date = request.POST['date']
        start_hours = request.POST['start_hours']
        end_hours = request.POST['end_hours']
        client_id = request.POST['select_client']
        theme_id = request.POST['select_theme']
        price = RentBusiness().calc_desconto(date, client_id, theme_id)
        street = request.POST['street']
        number = request.POST['number']
        complement = request.POST['complement']
        district = request.POST['district']
        city = request.POST['city']
        state = request.POST['state']

        RentDao().saveRent(
            date,
            start_hours,
            end_hours,
            client_id,
            theme_id,
            price,
            street,
            number,
            complement,
            district,
            city,
            state
        )

        return redirect('/listRent')

    #Deleta um aluguel e volta para listagem de alugueis
    def deleteRent(request, id):
        RentDao().deleteRent(id)
        return redirect('/listRent')
    
    #Pega um aluguel pelo ID e enviar para o form de edição
    def detailRent(request, id):
        rent = RentDao().getRent(id)
        return render(request, 'rent/formEditRent.html', {'rent': rent})
    
    #Atualiza um item e volta para listagem
    def updateRent(request, id):
        date = request.POST['date']
        start_hours = request.POST['start_hours']
        end_hours = request.POST['end_hours']
        client_id = request.POST['select_client']
        theme_id = request.POST['select_theme']
        price = RentBusiness().calc_desconto(date, client_id, theme_id)
        street = request.POST['street']
        number = request.POST['number']
        complement = request.POST['complement']
        district = request.POST['district']
        city = request.POST['city']
        state = request.POST['state']
        RentDao().updateRent(
            id,
            date,
            start_hours,
            end_hours,
            client_id,
            theme_id,
            price,
            street,
            number,
            complement,
            district,
            city,
            state
        )

        return redirect('/listRent')