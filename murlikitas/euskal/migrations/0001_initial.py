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
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_left_choice', models.CharField(default=b'', max_length=128)),
                ('second_left_choice', models.CharField(default=b'', max_length=128)),
                ('third_left_choice', models.CharField(default=b'', max_length=128)),
                ('first_right_choice', models.CharField(default=b'', max_length=128)),
                ('second_right_choice', models.CharField(default=b'', max_length=128)),
                ('third_right_choice', models.CharField(default=b'', max_length=128)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
