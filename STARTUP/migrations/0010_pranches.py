# Generated by Django 4.0.6 on 2022-07-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STARTUP', '0009_projects_had_done_client_projects_had_done_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pranches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
