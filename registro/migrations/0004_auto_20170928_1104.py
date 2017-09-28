# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20170928_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Responsable'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.TipoDeEquipo'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='zona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registro.Zona'),
        ),
    ]
