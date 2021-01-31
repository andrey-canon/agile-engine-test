"""Accounting urls"""
from django.urls import include, path

from apps.accounting.api import urls
from apps.accounting.views import index

urlpatterns = [
    path('api/', include(urls, namespace='api')),
    path('transactions/', index),
]
