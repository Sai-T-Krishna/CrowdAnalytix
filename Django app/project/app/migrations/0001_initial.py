# Generated by Django 4.0.6 on 2022-07-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateField(auto_created=True)),
                ('start_date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('descriptioon', models.CharField(max_length=1000)),
                ('duration', models.DurationField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]