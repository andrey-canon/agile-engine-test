"""Model file"""
from django.contrib.auth.models import User
from django.db import models

from apps.accounting.constants import CREDIT_LABEL, DEBIT_LABEL


class Account(models.Model):
    """Account Model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    balance = models.IntegerField(default=0)


class Transaction(models.Model):
    """Transaction Model"""

    TRANSACTION_TYPES = [
        (CREDIT_LABEL, "Credit"),
        (DEBIT_LABEL, "Debit")
    ]

    created = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default=0)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
