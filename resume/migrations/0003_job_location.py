# Generated by Django 2.2 on 2019-04-10 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_job_companyurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
    ]
