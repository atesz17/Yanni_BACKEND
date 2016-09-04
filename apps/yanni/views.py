from django.views.generic import ListView

from apps.yanni.models import CuttingWheel


class CuttingWheelList(ListView):
    model = CuttingWheel