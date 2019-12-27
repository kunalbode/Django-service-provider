from django.urls import path
from . import views


urlpatterns=[
    path('', views.indexPage, name='seller_index'),
    path('SellerActivity/', views.pendingactivityPage, name='SellerActivity'),
    path('AddDetail/', views.AddDetail, name='AddDetail'),


]

