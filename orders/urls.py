from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_order, name='place_order'),
    path('orders/', views.order_list, name='order_list'),
]
