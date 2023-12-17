from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.TextField()
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("core:product", kwargs={"slug": self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={"slug": self.slug})
    
    def get_remove_from_cart_url(self):
        print("enter in REMOVE")
        return reverse("core:remove-from-cart", kwargs={"slug": self.slug})
    


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item =models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered =  models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    def get_total_price(self):
        return self.quantity * self.item.price
    


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items= models.ManyToManyField(OrderItem)
    start_date= models.DateTimeField(auto_now_add=True) 
    ordered_date=models.DateTimeField()
    ordered =  models.BooleanField(default=False)

    
    def get_final_price(self):
        total  = 0
        for order_item in self.items.all():
            total += order_item.get_total_price()
        return total