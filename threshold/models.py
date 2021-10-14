from django.db import models
from django.utils import timezone

class SetThreshold(models.Model):
    threshold = models.PositiveIntegerField(verbose_name='임계치')
    set_date = models.DateTimeField(verbose_name='등록시간', default=timezone.now)

    def __str__(self):
        return str(self.threshold)
