# Generated by Django 3.2.5 on 2021-09-16 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alteernlingual_topic', '0008_readcount'),
        ('alteernlingual_subjects', '0003_auto_20210916_0821'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
    ]
