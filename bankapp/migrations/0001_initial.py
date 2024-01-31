# Generated by Django 4.2.2 on 2024-01-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('bmi', models.FloatField()),
                ('smoker', models.CharField(max_length=3)),
                ('region', models.CharField(max_length=20)),
                ('children', models.IntegerField()),
            ],
        ),
    ]
