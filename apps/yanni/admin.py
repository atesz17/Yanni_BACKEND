from django.contrib import admin

from .models import CuttingDisc, TopicNumber, PartNumber, Manufacturer

admin.site.register(CuttingDisc)
admin.site.register(TopicNumber)
admin.site.register(PartNumber)
admin.site.register(Manufacturer)
