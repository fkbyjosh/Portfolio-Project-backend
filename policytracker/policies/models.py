from django.db import models

# Create your models here.
from django.db import models

class Policy(models.Model):
    policy_id = models.CharField(max_length=50, unique=True)
    client_name = models.CharField(max_length=100)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20)  # e.g., "paid", "unpaid"
    assigned_status = models.CharField(max_length=20)  # e.g., "approved", "rejected", "pended"
    date_processed = models.DateField(auto_now=True)

    def __str__(self):
        return self.policy_id
