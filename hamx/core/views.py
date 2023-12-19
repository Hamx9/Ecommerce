from django.shortcuts import get_object_or_404, redirect, render
from .models import Item, Order,OrderItem
from django.utils import timezone
from django.views.generic import ListView, DetailView,View
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin 
from .form import CheckOut
#

#  Create your views here.
# def item_list(request):
#     context = {
#         'items':Item.objects.all(),
        
#     }
#     return render(request,"home-page.html",context)


class  HomeView (ListView):
    model = Item
    template_name = "home.html"


 
#summery view
class OrderSummeryView(LoginRequiredMixin,View):
   def get(self,*args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user,ordered=False)
            print(order.items)
            context = {
                'object':order
            }
            return render(self.request,"order_summery.html",context)
        except ObjectDoesNotExist:
            print("enter in except")
            messages.error(self.request,"you do not have active order")
            return redirect("/")

class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckOut()
        context={
            'form' : form
        } 
        return render(self.request,'checkout.html', context)
    def post(self, *args, **kwargs):
        form = CheckOut(self.request.POST or None)
        if form.is_valid():
            print("the form is vlaid")
            return redirect('core:checkout')




class  ItemDetailView (DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item,slug=slug)
    order_item , created =OrderItem.objects.get_or_create(item = item, user = request.user,ordered =False)
    order_qs= Order.objects.filter(user= request.user, ordered =False)
   
    if order_qs.exists() :
        order =order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request,"this item was quantity updated")
        else:
            order.items.add(order_item)
            messages.info(request,"this item was added to you cart")
    else:
        ordered_date = timezone.now()
       
        order = Order.objects.create(user =request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"this item was added to cart")
    return redirect("core:product",slug =slug) 


def remove_from_cart(request,slug):
    item = get_object_or_404(Item,slug=slug)
    order_qs= Order.objects.filter(user= request.user, ordered =False)
    print(order_qs)
    if order_qs.exists() :
        order =order_qs[0]
        #check if the item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item,user= request.user,ordered =False)[0]
            order.items.remove(order_item)
            messages.info(request,"this item is removed from cart")
        else:
            # add msg syaing item does not in order 
            messages.info(request,"item does not exist in you cart")
            return redirect("core:product",slug =slug) 
    else:
        messages.info(request,"you do not have a active order")
        return redirect("core:product",slug =slug) 
    return redirect("core:product",slug =slug) 






