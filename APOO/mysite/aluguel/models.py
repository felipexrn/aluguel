from django.db import models
from django.db.models.deletion import CASCADE

class Client(models.Model):
    name = models.CharField(max_length=60, blank=False)
    email = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return self.name

class Phone(models.Model):
    ddd = models.CharField(max_length=3)
    number = models.CharField(max_length=10)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='phones')
    
    def __str__(self):
        return self.client.name + ' ' + self.ddd + ' '+ self.number
    
    
class Theme(models.Model):
    name = models.CharField(max_length=20, blank=False)
    color = models.CharField(max_length=10)
    price = models.FloatField()
    itens =  models.ManyToManyField('Item', related_name='themes')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=200)
    #theme = models.ForeignKey('Theme', on_delete=models.CASCADE, related_name='itens')

    def __str__(self):
        return self.name

class Rent(models.Model):
    date = models.DateField(blank=False, null=False)
    start_hours = models.TimeField(auto_now=True, blank=False, null=False)
    end_hours = models.TimeField(auto_now=True, blank=False, null=False)
    price = models.FloatField(default=0.0)
    street = models.CharField(max_length=60, default="")
    number = models.IntegerField(null=True)
    complement = models.CharField(max_length=50, default="")
    district = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=20, blank=True)
    client = models.ForeignKey('Client', on_delete=CASCADE, related_name='rents')
    theme = models.ForeignKey('Theme', on_delete=CASCADE, related_name='rents')
    
    def __str__(self):
        return str(self.date) + ' ' + self.client.name + ' ' + self.theme.name

    
