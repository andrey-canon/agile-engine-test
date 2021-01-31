from rest_framework import serializers
from crum import get_current_user

from apps.accounting.models import Transaction, Account
from apps.accounting.constants import CREDIT_LABEL, DEBIT_LABEL


class TransactionsSerializer(serializers.ModelSerializer):
    """
    Serializer class for Trasaction.
    """

    class Meta(object):
        """
        Define the model and the allowed fields.
        """
        model = Transaction
        fields = ['transaction_type', 'amount', 'id']

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        amount = validated_data.get('amount')

        if amount < 0:
            raise serializers.ValidationError('The amount must be a positive value')

        if validated_data.get('transaction_type', '') == DEBIT_LABEL:
            account = self._get_current_account()

            if account.balance - amount < 0:
                raise serializers.ValidationError('The amount is higher that the current account balance')

        return validated_data

    def create(self, validated_data):
        """
        """
        account = self._get_current_account()
        amount = validated_data.get('amount', 0)
        transaction_type = validated_data.get('transaction_type', '')

        if transaction_type == CREDIT_LABEL:
            account.balance += amount
        elif transaction_type == DEBIT_LABEL:
            account.balance -= amount

        account.save()

        return Transaction.objects.create(account=account, amount=amount, transaction_type=transaction_type)

    def _get_current_account(self):
        user = get_current_user()
        user = user if user.is_authenticated else None
        account, _ = Account.objects.get_or_create(user=user)
        return account
