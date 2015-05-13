from django.db import models


class Mission(models.Model):
    lat = models.FloatField(max_length=128, default=0)
    lng = models.FloatField(max_length=128, default=0)
    title = models.CharField(max_length=128, default='')

    def __unicode__(self):
        return self.title
