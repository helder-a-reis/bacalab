# Generated by Django 2.2 on 2019-05-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20190410_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='jobType',
            field=models.CharField(choices=[('PROF', 'Professional'), ('EDU', 'Education')], default='PROF', max_length=10),
        ),
    ]
