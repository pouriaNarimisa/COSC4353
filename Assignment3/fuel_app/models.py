from django.db import models
from django.conf import settings
# Create your models here.
class Client(models.Model):
    # by default, there is a field called id , so no need to specify it
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #Client profile management 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)

class Quote(models.Model):
    # by default, there is a field called id which is the pk of the table, so no need to specify it
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    address = models.CharField(max_length=100)
    gallons = models.IntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2)