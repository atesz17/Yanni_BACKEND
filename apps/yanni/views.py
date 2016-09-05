from django.views.generic import ListView

from .models import CuttingDisc


class CuttingDiscList(ListView):
    model = CuttingDisc