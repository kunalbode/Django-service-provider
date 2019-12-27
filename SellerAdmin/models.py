from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class SellerAdmin(models.Model):
    name = models.CharField(max_length=20, verbose_name="Enter Full Name")

class ServiceType(models.Model):
    service_name=models.CharField(max_length=30)
    description=models.TextField()

    def __str__(self):
        return self.service_name

class SubService(models.Model):
    sub_name= models.TextField()
    category = models.ForeignKey(ServiceType(),on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_name


class Service(models.Model):
    type = models.ForeignKey(ServiceType,on_delete=models.CASCADE)
    sub_category=models.ForeignKey(SubService,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description=models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()
    discount = models.IntegerField()
    seller = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.title


