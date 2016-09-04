from django.conf.urls import url

from .views import CuttingWheelList

urlpatterns = [
    url(r'^$', CuttingWheelList.as_view())
]