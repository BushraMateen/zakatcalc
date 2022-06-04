from django.db import models


class ZakatTable(models.Model):
    Line = models.IntegerField()
    name = models.CharField(max_length = 500)
    category = models.CharField(max_length = 500)
    AmtVal = models.IntegerField()
    ZakatRate = models.DecimalField(max_digits=15, decimal_places=2)
    ZakatDue = models.DecimalField(max_digits=15, decimal_places=2)
    

