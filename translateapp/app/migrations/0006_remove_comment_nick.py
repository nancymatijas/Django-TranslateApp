# Generated by Django 4.1.4 on 2023-01-26 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='nick',
        ),
    ]
