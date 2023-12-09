from django.shortcuts import get_object_or_404, redirect, render
from .models import Item, Order,OrderItem
from django.views.generic import ListView, DetailView
# Create your views here.
# def item_list(request):
#     context = {
#         'items':Item.objects.all(),
        
#     }
#     return render(request,"home-page.html",context)


class  HomeView (ListView):
    model = Item
    template_name = "home.html"


class  ItemDetailView (DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item,slug=slug)
    order_item =OrderItem.objects.create(item = item)
    order_qs= Order.objects.filter(user= request.user, ordered =False)
    if order_qs.exists() :
        order =order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
    else:
        order = Order.objects.create(user =request.user)
        order.items.add(order_item)
    return redirect("core:product",kwargs={
        'slug':slug
    }) 