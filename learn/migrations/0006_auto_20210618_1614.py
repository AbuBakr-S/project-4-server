# Generated by Django 3.2.4 on 2021-06-18 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learn', '0005_course_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='rating',
        ),
        migrations.CreateModel(
            name='CourseFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='learn.course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='feedback', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
