# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-04 12:45
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuttingWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Mérőlap szám')),
                ('stock_count', models.IntegerField(verbose_name='Gyártott/beérkezett darabszám')),
            ],
            options={
                'verbose_name_plural': 'Vágókorongok',
                'verbose_name': 'Vágókorong',
            },
        ),
        migrations.CreateModel(
            name='TopicNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_number', models.CharField(max_length=20, verbose_name='Témaszám')),
            ],
            options={
                'verbose_name_plural': 'Témaszámok',
                'verbose_name': 'Témaszám',
            },
        ),
        migrations.AddField(
            model_name='cuttingwheel',
            name='topic_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yanni.TopicNumber'),
        ),
    ]