# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-10 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_userprofile_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='company',
        ),
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_category', to='art.Categories'),
        ),
    ]
