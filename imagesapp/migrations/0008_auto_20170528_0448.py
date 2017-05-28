# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagesapp', '0007_remove_rate_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='image',
            field=models.ForeignKey(to='imagesapp.Image'),
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('image', 'user')]),
        ),
    ]
