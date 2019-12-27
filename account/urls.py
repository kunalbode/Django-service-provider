from django.urls import path
from . import views

urlpatterns=[
    path('', views.indexPage, name='index'),
    path('register/', views.register_user, name='register'),
    path('Sregister/', views.SRegisterPage, name='Sregister'),
    path('contact/', views.contactPage, name='contact'),
    path('service/', views.servicePage, name='service'),
    path('userlogin/', views.loginPage, name='userlogin'),
    path('sellerindex/', views.sellerindexPage, name='sellerindex'),
    path('repairS/', views.repairSPage, name='repairS'),
    path('SelfCare/', views.SelfCarePage, name='SelfCare'),
    path('HouseS/', views.houseSPage, name='HouseS'),
    path('otherS/', views.otherSPage, name='otherS'),
    path('logout/', views.logout_page, name='logout'),

    # path('forgot/', views.forgot, name='forgot')

]

