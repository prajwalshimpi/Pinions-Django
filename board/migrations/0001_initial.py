# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('usernames', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('category', models.CharField(max_length=200)),
                ('docfile', models.FileField(upload_to='img')),
                ('link', models.URLField()),
                ('imglink', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(unique=True, max_length=70)),
                ('password', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('location', models.CharField(max_length=400)),
                ('profilepic', models.FileField(upload_to='img')),
            ],
        ),
    ]
