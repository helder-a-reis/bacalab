# Generated by Django 2.2 on 2019-04-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190418_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumb',
            field=models.ImageField(default='project.png', upload_to=''),
        ),
    ]
