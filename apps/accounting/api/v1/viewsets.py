"""Viewsets file"""
from rest_framework import viewsets

from apps.accounting.api.v1.serializers import TransactionsSerializer
from apps.accounting.models import Transaction


class TransactionViewSet(viewsets.ModelViewSet):
    """Main viewset for Transactions."""

    serializer_class = TransactionsSerializer
    queryset = Transaction.objects.all()
