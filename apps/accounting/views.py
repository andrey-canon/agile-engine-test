from django.http import HttpResponse
from django.template import loader

from apps.accounting.models import Transaction, Account


def index(request):
    user = request.user
    user = user if user.is_authenticated else None
    account, _ = Account.objects.get_or_create(user=user)
    transaction_list = Transaction.objects.filter(account=account)
    template = loader.get_template('accounting/index.html')
    context = {
        'transaction_list': transaction_list,
    }
    return HttpResponse(template.render(context, request))
