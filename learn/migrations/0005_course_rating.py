# Generated by Django 3.2.4 on 2021-06-17 17:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_rename_rating_course_rating_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]