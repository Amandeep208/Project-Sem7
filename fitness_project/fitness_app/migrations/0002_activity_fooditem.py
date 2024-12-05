# Generated by Django 5.1.4 on 2024-12-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('calories_burned', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('calories', models.IntegerField()),
            ],
        ),
    ]
