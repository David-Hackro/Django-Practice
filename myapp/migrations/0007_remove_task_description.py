# Generated by Django 5.0.2 on 2024-02-16 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_task_description_task_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
