# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_choice', models.CharField(default=b'', max_length=128)),
                ('second_choice', models.CharField(default=b'', max_length=128)),
                ('third_choice', models.CharField(default=b'', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('left_choices', models.OneToOneField(related_name=b'left_choices', null=True, to='euskal.Choices')),
                ('right_choices', models.OneToOneField(related_name=b'right_choices', null=True, to='euskal.Choices')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='user_profile',
            field=models.OneToOneField(to='euskal.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choices',
            name='user_preferences',
            field=models.ForeignKey(to='euskal.UserPreferences'),
            preserve_default=True,
        ),
    ]
