# Generated by Django 3.2.5 on 2021-09-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alteernlingual_topic', '0024_auto_20210928_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopicdetails',
            name='audio_file_ig',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/audios/default.mp3', null=True, upload_to='audios_ig/'),
        ),
    ]