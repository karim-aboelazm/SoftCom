# Generated by Django 4.0.6 on 2022-07-14 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('privacy', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone_No', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('fb_link', models.URLField(blank=True)),
                ('tw_link', models.URLField(blank=True)),
                ('ln_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='team/')),
                ('job', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='services/')),
            ],
        ),
        migrations.CreateModel(
            name='Projects_had_not_done',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='pro_had_not_finished/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='STARTUP.job_categories')),
            ],
        ),
        migrations.CreateModel(
            name='Projects_had_done',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='pro_had_finished/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='STARTUP.job_categories')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='STARTUP.job_categories')),
            ],
        ),
    ]
