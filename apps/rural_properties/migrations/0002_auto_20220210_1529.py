# Generated by Django 2.2.24 on 2022-02-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rural_properties', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruralproperty',
            name='city',
        ),
        migrations.AlterField(
            model_name='ruralproperty',
            name='tipe',
            field=models.CharField(default='Rural', editable=False, max_length=5),
        ),
    ]
