# Generated by Django 2.0.4 on 2018-04-23 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcribe', '0002_auto_20180423_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='fileid',
        ),
        migrations.AddField(
            model_name='text',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]