# Generated by Django 2.2 on 2019-04-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='teaser',
            field=models.TextField(max_length=200),
        ),
    ]
