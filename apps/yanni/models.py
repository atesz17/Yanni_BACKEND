from django.db import models

from utils.models import TimeStampedModel


class TopicNumber(TimeStampedModel):
    """Témaszámot reprezentáló model"""

    topic_number = models.CharField("Témaszám", max_length=20)

    def __str__(self):
        return self.topic_number

    class Meta:
        verbose_name = "Témaszám"
        verbose_name_plural = "Témaszámok"


class CuttingWheel(TimeStampedModel):
    """Vágókorongot reprezentáló model"""

    # TODO: merolapszam?
    id = models.AutoField("Mérőlap szám", primary_key=True, auto_created=True)
    stock_count = models.IntegerField("Gyártott/beérkezett darabszám")
    topic_number = models.ForeignKey(TopicNumber, on_delete=models.CASCADE) # TODO: ebben az oszlopban meg tobb dolog fel van tuntetve

    class Meta:
        verbose_name = "Vágókorong"
        verbose_name_plural = "Vágókorongok"
