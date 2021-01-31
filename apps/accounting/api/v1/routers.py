"""Router file."""
from rest_framework import routers

from apps.accounting.api.v1.viewsets import TransactionViewSet

router = routers.DefaultRouter()
router.register(r'', TransactionViewSet)
