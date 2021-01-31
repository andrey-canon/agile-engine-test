"""Api urls file"""
from django.urls import include, path

from apps.accounting.api.v1 import urls

app_name = 'accounting'

urlpatterns = [
    path('v1/', include(urls, namespace='v1'))
]
