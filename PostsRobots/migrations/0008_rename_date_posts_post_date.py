# Generated by Django 5.1.3 on 2024-11-16 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PostsRobots', '0007_alter_posts_bronze_trophies_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='date',
            new_name='post_date',
        ),
    ]
