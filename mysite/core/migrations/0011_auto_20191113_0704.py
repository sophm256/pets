# Generated by Django 2.2.5 on 2019-11-13 13:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_pet_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartStopTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_start_or_stop', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_or_stop_type', models.SmallIntegerField(choices=[(1, 'start'), (2, 'stop')])),
            ],
        ),
        migrations.RemoveField(
            model_name='startendperiod',
            name='search_party_member',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='age',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='searchpartymembers',
            name='search_instance',
        ),
        migrations.AddField(
            model_name='pet',
            name='date_last_seen',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='pet',
            name='last_known_location',
            field=models.CharField(default='unknown', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='remarks',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='pet',
            name='time_last_seen',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='searchpartymembers',
            name='pet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Pet'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=15, verbose_name='Name of Pet'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='pet',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='pet_images', verbose_name='Photo of Your Pet'),
        ),
        migrations.AlterField(
            model_name='searchpartymembers',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SearchInstance',
        ),
        migrations.DeleteModel(
            name='StartEndPeriod',
        ),
        migrations.AddField(
            model_name='startstoptime',
            name='search_party_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SearchPartyMembers'),
        ),
    ]
