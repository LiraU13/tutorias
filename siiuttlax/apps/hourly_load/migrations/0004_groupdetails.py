# Generated by Django 5.0.6 on 2024-05-31 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('hourly_load', '0003_concept_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField(default=0, verbose_name='Horas')),
                ('concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hourly_load.concept')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.group')),
            ],
            options={
                'verbose_name': 'Detalle del grupo',
                'verbose_name_plural': 'Detalles del grupo',
            },
        ),
    ]