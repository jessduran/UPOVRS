# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rentedequipment_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentedequipment',
            name='equipment_id',
            field=models.DecimalField(decimal_places=0, max_digits=4, null=True),
        ),
    ]
