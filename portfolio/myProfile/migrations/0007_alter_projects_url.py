# Generated by Django 4.2.6 on 2023-10-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProfile', '0006_remove_projects_professional_projects_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
