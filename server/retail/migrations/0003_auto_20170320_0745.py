# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import retail.models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0002_sequence'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequence',
            name='name',
            field=models.CharField(default='adaf', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sequence',
            name='owner',
            field=models.CharField(default='afdafa', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sequence',
            name='design',
            field=models.TextField(validators=[retail.models.validate_sequence_design]),
        ),
    ]
