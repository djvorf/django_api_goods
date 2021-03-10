import uuid

from django.db import models

from model_utils.models import TimeStampedModel


class Goods(TimeStampedModel):
    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4, editable=False)
    where_from = models.CharField('Откуда', max_length=200)
    where_to = models.CharField('Куда', max_length=200)
    date = models.DateField('Когда')
    time = models.TimeField('Во-сколько')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'
