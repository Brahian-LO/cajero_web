# Generated by Django 5.2.1 on 2025-05-14 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CajeroUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.PositiveIntegerField(unique=True)),
                ('saldo', models.FloatField(default=0)),
            ],
        ),
    ]
