# Generated by Django 5.1.4 on 2024-12-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('calories_burned', models.FloatField()),
            ],
            options={
                'verbose_name': 'Exercise',
                'verbose_name_plural': 'Exercises',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('calories', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
            },
        ),
    ]