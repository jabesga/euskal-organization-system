from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    has_voted_group_name = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class UserPreferences(models.Model):
    user_profile = models.OneToOneField(UserProfile)
    left_choices = models.OneToOneField('Choices', null=True, related_name='left_choices')
    right_choices = models.OneToOneField('Choices', null=True, related_name='right_choices')

    def __unicode__(self):
        return 'Preferences of %s %s' % (self.user_profile.user.first_name, self.user_profile.user.last_name)


class Choices(models.Model):
    user_preferences = models.ForeignKey(UserPreferences)
    first_choice = models.CharField(max_length=128, default='')
    second_choice = models.CharField(max_length=128, default='')
    third_choice = models.CharField(max_length=128, default='')

    def __unicode__(self):
        return 'FC: %s, SC: %s, TC: %s' % (self.first_choice, self.second_choice, self.third_choice)


class Option(models.Model):
    option_name = models.CharField(max_length=128, default='')
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.option_name

