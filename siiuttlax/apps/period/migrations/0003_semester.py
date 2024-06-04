# Generated by Django 5.0.6 on 2024-06-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('period', '0002_alter_period_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=1, verbose_name='Cuatrimestre')),
                ('semester_name', models.CharField(max_length=10, verbose_name='Cuatrimestre en Letra')),
                ('short_name', models.CharField(max_length=5, verbose_name='Abreviatura')),
            ],
            options={
                'verbose_name': 'Cuatrimestre',
                'verbose_name_plural': 'Cuatrimestres',
            },
        ),
    ]