# Generated by Django 3.2.5 on 2021-08-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alteernlingual_user', '0008_topic_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='category',
        ),
        migrations.AlterField(
            model_name='profile',
            name='loi',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'English'), (2, 'Igbo'), (3, 'Hausa'), (4, 'Yoruba'), (5, 'French'), (6, 'Arabic')], null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ltl',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'English'), (2, 'Igbo'), (3, 'Hausa'), (4, 'Yoruba'), (5, 'French'), (6, 'Arabic')], null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
