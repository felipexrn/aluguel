from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=200)
    #theme = models.ForeignKey('Theme', on_delete=models.CASCADE, related_name='itens')

    def __str__(self):
        return self.name
