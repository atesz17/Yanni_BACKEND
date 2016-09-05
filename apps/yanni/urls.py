from django.conf.urls import url

from .views import CuttingDiscList

app_name = "yanni"
urlpatterns = [
    url(r'^$', CuttingDiscList.as_view(), name='cutting-wheel-list')
]