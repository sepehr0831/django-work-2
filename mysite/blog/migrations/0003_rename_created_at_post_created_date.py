# Generated by Django 4.0.4 on 2022-05-10 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_counted_view_post_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created_date',
        ),
    ]
