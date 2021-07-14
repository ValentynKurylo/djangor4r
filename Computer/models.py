from django.db import models

class ComputerModel(models.Model):
    class Meta:
        db_table = 'comouter'

    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    memory = models.IntegerField()
    procesor = models.FloatField()
    monitor = models.IntegerField()
