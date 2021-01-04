from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class ShtuffList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
       
    def get_absolute_url(self):
        return reverse('shtuff_lists_index')

class Shtuff(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    
    shtuff_list = models.ForeignKey(ShtuffList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shtuff_list_detail', kwargs={'shtuff_list_id':self.shtuff_list.id})