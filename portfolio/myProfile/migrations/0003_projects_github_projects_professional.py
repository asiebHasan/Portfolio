# Generated by Django 4.2.6 on 2023-10-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProfile', '0002_image_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='github',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='professional',
            field=models.BooleanField(default=False),
        ),
    ]
