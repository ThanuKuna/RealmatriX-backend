# Generated by Django 5.0 on 2024-01-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealmatriX', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('nic', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('phoneno', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]