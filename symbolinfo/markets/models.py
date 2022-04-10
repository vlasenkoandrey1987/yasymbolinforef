from django.db import models


class Market(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)


class SymbolInfo(models.Model):
    name = models.CharField(max_length=20)
    market = models.ForeignKey(
        Market,
        on_delete=models.CASCADE,
        related_name='symbols',
    )
    lot_size = models.IntegerField(default=1)
