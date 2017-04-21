# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesapp', '0006_auto_20170421_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='value',
        ),
    ]
