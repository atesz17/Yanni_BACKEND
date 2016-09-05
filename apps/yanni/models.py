from django.db import models

from utils.models import TimeStampedModel


class TopicNumber(TimeStampedModel):
    """Témaszámot reprezentáló model"""

    topic_number = models.CharField("Témaszám", max_length=20, unique=True)

    def __str__(self):
        return self.topic_number

    class Meta:
        verbose_name = "Témaszám"
        verbose_name_plural = "Témaszámok"


class PartNumber(TimeStampedModel):
    """Cikkszámot reprezentáló model"""
    part_number = models.CharField("Cikkszám", max_length=20, unique=True)

    def __str__(self):
        return self.part_number

    class Meta:
        verbose_name = "Cikkszám"
        verbose_name_plural = "Cikkszámok"


class Manufacturer(TimeStampedModel):
    """Gyártót reprezentáló model"""
    name = models.CharField("Név", max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gyártó"
        verbose_name_plural = "Gyártók"


class CuttingDisc(TimeStampedModel):
    """Vágókorongot reprezentáló model"""

    # TODO: merolapszam?
    id = models.AutoField("Mérőlap szám", primary_key=True, auto_created=True)
    stock_count = models.IntegerField("Gyártott/beérkezett darabszám")
    # TODO: on_delete=model.SET_NULL ?
    topic_number = models.ForeignKey(TopicNumber, on_delete=models.CASCADE, verbose_name="Témaszám") # TODO: ebben az oszlopban meg tobb dolog fel van tuntetve
    # TODO: on_delete=model.SET_NULL ?
    part_number = models.ForeignKey(PartNumber, on_delete=models.CASCADE, verbose_name="Cikkszám")
    type_of_shape = models.IntegerField("Alakjel")
    nominal_diameter = models.IntegerField("Névleges átmérő (mm)")
    nominal_thickness = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Névleges vastagság (mm)")
    nominal_mortise = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Névleges furat (mm)")
    # TODO: on_delete=model.SET_NULL ?
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Gyártó")


    class Meta:
        verbose_name = "Vágókorong"
        verbose_name_plural = "Vágókorongok"
