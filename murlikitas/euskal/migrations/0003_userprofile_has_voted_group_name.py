# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euskal', '0002_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='has_voted_group_name',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
