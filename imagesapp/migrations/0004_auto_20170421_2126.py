# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesapp', '0003_auto_20170421_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='owner',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='size',
        ),
        migrations.AddField(
            model_name='rate',
            name='rating',
            field=models.PositiveSmallIntegerField(default=3, verbose_name=b'Rating (stars)', choices=[(1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five')]),
        ),
    ]
