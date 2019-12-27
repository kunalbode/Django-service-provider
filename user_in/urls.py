from django.urls import path
from . import views

urlpatterns=[
    path('ram/', views.user_index, name='userindex'),
    path('cart/', views.cart, name='cart'),
    path('details/<int:pk>', views.details, name='details'),
    path('add_cart/<int:pk>', views.add_cart, name='add_cart')
]
