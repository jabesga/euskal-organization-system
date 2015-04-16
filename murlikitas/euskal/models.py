from django.db import models
from django.contrib.auth.models import User


class UserPreferences(models.Model):
    user = models.ForeignKey(User)
    first_left_choice = models.CharField(max_length=128, default='')
    second_left_choice = models.CharField(max_length=128, default='')
    third_left_choice = models.CharField(max_length=128, default='')
    first_right_choice = models.CharField(max_length=128, default='')
    second_right_choice = models.CharField(max_length=128, default='')
    third_right_choice = models.CharField(max_length=128, default='')

    def __unicode__(self):
        return self.user.username