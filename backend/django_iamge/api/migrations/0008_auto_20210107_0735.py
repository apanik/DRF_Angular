# Generated by Django 3.1.5 on 2021-01-07 07:35

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210107_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default=django.utils.timezone.now, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True, default=datetime.datetime(2021, 1, 7, 7, 35, 12, 956896, tzinfo=utc)),
            preserve_default=False,
        ),
    ]