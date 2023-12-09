from django.shortcuts import render
from .models import Item
# Create your views here.
def item_list(request):
    context = {
        'items':Item.objects.all(),
        'test' : [1,2,3,4,4,5,6]
    }
    return render(request,"home-page.html",context)
    