# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0002_auto_20160925_2251'),
        ('fall_assignment', '0004_auto_20160926_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='quote',
        ),
        migrations.AddField(
            model_name='favorite',
            name='quote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='fall_assignment.Quote'),
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='user',
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='login_reg.User'),
        ),
    ]