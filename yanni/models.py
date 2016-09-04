from django.db import models


class CuttingWheel(models.Model):
    # TODO: merolapszam?
    stock_count = models.IntegerField("Gyártott/beérkezett darabszám")
    topic_number = models.ForeignKey(TopicNumber, on_delete=models.CASCADE) # TODO: ebben az oszlopban meg tobb dolog fel van tuntetve

    class Meta:
        verbose_name = "Vágókorong"
        verbose_name_plural = "Vágókorongok"


class TopicNumber(models.Model):
    topic_number = models.CharField("Témaszám", max_length=20)

    class Meta:
        verbose_name = "Témaszám"
        verbose_name_plural = "Témaszámok"