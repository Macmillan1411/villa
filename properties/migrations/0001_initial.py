# Generated by Django 4.2.15 on 2024-08-08 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to=None)),
                ('description', models.TextField()),
                ('space', models.IntegerField()),
                ('floor_number', models.IntegerField()),
                ('bathrooms', models.PositiveIntegerField()),
                ('bedrooms', models.PositiveIntegerField()),
                ('rooms', models.PositiveIntegerField()),
                ('parking', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.propertycategory')),
            ],
        ),
    ]
