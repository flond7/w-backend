# Generated by Django 4.0.3 on 2022-03-24 09:55

import api.models
from django.db import migrations, models
import djongo.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='path',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('pathId', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True)),
            ],
            options={
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='woman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('surname', models.CharField(blank=True, default='', max_length=100)),
                ('path', djongo.models.fields.ArrayField(model_container=api.models.path)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
