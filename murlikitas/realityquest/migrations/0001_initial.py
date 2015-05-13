# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField(default=0, max_length=128)),
                ('lng', models.FloatField(default=0, max_length=128)),
                ('title', models.CharField(default=b'', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
