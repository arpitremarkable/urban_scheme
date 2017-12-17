# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import emi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EMIRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('bank', models.CharField(max_length=50)),
                ('tenure', models.IntegerField(help_text='In months')),
                ('rate', models.IntegerField(help_text='Interest rate in percentage')),
                ('amount', models.IntegerField(help_text='Minimum loan amount')),
            ],
            options={
                'abstract': False,
            },
            bases=(emi.models.AbstractBaseModel, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='emirate',
            unique_together=set([('bank', 'tenure')]),
        ),
    ]
