# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-06-06 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='题目')),
                ('type_id', models.IntegerField(verbose_name='类型id')),
                ('type', models.CharField(max_length=100, verbose_name='类型')),
                ('answer', models.CharField(max_length=2000, verbose_name='答案')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('reason', models.CharField(max_length=100, verbose_name='删除理由')),
            ],
            options={
                'verbose_name': '试题表',
                'verbose_name_plural': '试题表',
                'db_table': 'questions',
            },
        ),
    ]