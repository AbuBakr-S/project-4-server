# Generated by Django 3.2.4 on 2021-06-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0010_course_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=models.TextField(max_length=1350),
        ),
    ]
