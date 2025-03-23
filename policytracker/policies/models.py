from django.db import models

# Create your models here.

class Policy(models.Model):
    policy_num = models.IntegerField(primary_key=True)
    policy_holder = models.CharField(max_length=100)
    policy_type = models.CharField(max_length=50)
    payment_mode = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    premium = models.DecimalField(max_digits=10, decimal_places-2)
