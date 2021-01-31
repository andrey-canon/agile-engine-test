"""
"""
from django.urls import include, path

from apps.accounting.api.v1.routers import router

app_name = 'accounting'

urlpatterns = [
    path('transactions/', include((router.urls, 'accounting'), namespace='routers'))
]
