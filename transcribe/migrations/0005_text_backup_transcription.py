# Generated by Django 2.0.4 on 2018-04-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcribe', '0004_pendingtranscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='backup_transcription',
            field=models.TextField(blank=True),
        ),
    ]
