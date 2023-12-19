from django.urls import path 
from .views import HomeView, ItemDetailView,add_to_cart,remove_from_cart,OrderSummeryView,CheckoutView
app_name ='core'

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('product/<slug>/',ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/',add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart, name='remove-from-cart'),
    path('order-summery/',OrderSummeryView.as_view(), name='order-summery'),
    path('checkout/',CheckoutView.as_view(), name='checkout'),
]
