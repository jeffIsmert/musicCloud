# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170409_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='is_fave',
            new_name='is_favorite',
        ),
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default=b'', upload_to=b''),
        ),
    ]
