# Generated by Django 3.2.4 on 2021-06-17 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_course_rated_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='rated_by',
            new_name='rating',
        ),
    ]