# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0002_auto_20160925_2251'),
        ('fall_assignment', '0003_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='favorite',
            name='quote',
            field=models.ManyToManyField(related_name='quotes', to='fall_assignment.Quote'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ManyToManyField(related_name='users', to='login_reg.User'),
        ),
    ]