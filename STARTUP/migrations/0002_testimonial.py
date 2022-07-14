# Generated by Django 4.0.6 on 2022-07-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STARTUP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='testimonial/')),
                ('letter', models.TextField()),
            ],
        ),
    ]
