# Generated by Django 2.2.5 on 2019-11-11 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_customuser_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='image',
            new_name='profile_image',
        ),
    ]
