from django.views.generic import ListView

from .models import CuttingWheel


class CuttingWheelList(ListView):
    model = CuttingWheel