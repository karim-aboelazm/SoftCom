# Generated by Django 4.0.6 on 2022-07-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STARTUP', '0008_projects_had_done_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects_had_done',
            name='client',
            field=models.CharField(default='', max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects_had_done',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projects_had_done',
            name='project_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projects_had_done',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
