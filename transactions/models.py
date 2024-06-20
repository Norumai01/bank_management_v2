from django.db import models
from customers.models import Account
from django.utils import timezone

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('DEPOSIT', 'Deposit')
        ('WITHDRAW', 'Withdraw')
        ('TRANSFER', 'Transfer')
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.account} - {self.transaction_type} - {self.amount}'