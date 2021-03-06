# Generated by Django 2.2.24 on 2022-02-10 15:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0005_auto_20220210_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuralProperty',
            fields=[
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_cadastral', models.CharField(max_length=25, null=True, unique=True)),
                ('registration_real_estate', models.CharField(max_length=8, null=True, unique=True)),
                ('country', models.CharField(default='Colombia', max_length=200)),
                ('department', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=400, unique=True)),
                ('tipe', models.CharField(default='Rural', max_length=5)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('owners', models.ManyToManyField(related_name='RuralProperty', to='owners.LandOwner')),
            ],
            options={
                'verbose_name': 'Rural Property',
                'verbose_name_plural': 'Rural Properties',
            },
        ),
    ]
