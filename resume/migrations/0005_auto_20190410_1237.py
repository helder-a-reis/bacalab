# Generated by Django 2.2 on 2019-04-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20190410_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='endYear',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
