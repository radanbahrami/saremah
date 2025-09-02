from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    renewal_date = models.DateField()
    notification_days_before = models.PositiveIntegerField(default=7)

    def __str__(self):
        return self.name
