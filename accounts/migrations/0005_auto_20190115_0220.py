# Generated by Django 2.1 on 2019-01-14 20:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190115_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 14, 20, 50, 46, 302473, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 14, 20, 50, 46, 302510, tzinfo=utc)),
        ),
    ]
