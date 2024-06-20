from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Holds user's information.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

# Holds all account types (checking, saving) for user.
class Account(models.Model):
    ACCOUNT_TYPES = [
        ('CHECKING', 'Checking')
        ('SAVING', 'Saving')
        ('MUTUALFUND', 'Mutual Fund')
        ('CERTDEPOSIT', 'Certificate of Deposit')
        ('MONEYMARKET', 'Money Market')
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.customer} - {self.account_type}: ${self.balance}'