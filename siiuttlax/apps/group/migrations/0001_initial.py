# Generated by Django 5.0.6 on 2024-05-31 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('career', '0001_initial'),
        ('period', '0002_alter_period_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fmonth_period', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1)),
                ('group', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F'), ('G', 'G'), ('H', 'H')], default='A', max_length=1)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.period')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'ordering': ['group'],
            },
        ),
    ]