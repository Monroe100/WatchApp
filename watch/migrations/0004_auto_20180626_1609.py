# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 13:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watch', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='businesss/')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Neighbourhood')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='business',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='watch.Business'),
            preserve_default=False,
        ),
    ]
