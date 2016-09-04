from django.conf.urls import url

from .views import CuttingWheelList

app_name = "yanni"
urlpatterns = [
    url(r'^$', CuttingWheelList.as_view(), name='cutting-wheel-list')
]