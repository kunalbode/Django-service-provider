from django.db import models

# Create your models here.

from django.db import models
from account.models import *
from SellerAdmin.models import Service
from django.contrib.auth import get_user_model
User=get_user_model()

class Cart(models.Model):

    product_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='customer')
    #seller = models.ForeignKey(User, on_delete=models.CASCADE,related_name='seller')


