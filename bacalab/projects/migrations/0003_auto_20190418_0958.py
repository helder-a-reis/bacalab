# Generated by Django 2.2 on 2019-04-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190412_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='thumb',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
