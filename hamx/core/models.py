from django.db import models
from django.conf import settings


# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    


class OrderItem(models.Model):
    item =models.models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.ti


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items= models.ManyToManyField(OrderItem)
    start_date= models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()
    Ordered =  models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
