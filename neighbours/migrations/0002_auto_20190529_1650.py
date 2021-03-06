# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-29 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post', models.TextField(blank=True)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('poster_id', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='posts',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbours.User'),
        ),
    ]
