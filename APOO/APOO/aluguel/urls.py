from django.urls import path

from .views import index, ItemViews

#URLs para página principal
    path('', index),

#URLs para CDUs Itens
    path('listItem/', ItemViews.listItem),
    path('formItem/', ItemViews.formItem),
    path('saveItem/', ItemViews.saveItem),
    path('deleteItem/<int:id>', ItemViews.deleteItem),
    path('detailItem/<int:id>', ItemViews.detailItem),
    path('updateItem/<int:id>', ItemViews.updateItem),