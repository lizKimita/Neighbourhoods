# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-30 08:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbours', '0007_posts_related_neighbourhood'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='related_neighbourhood',
            new_name='neighbourhood',
        ),
    ]
