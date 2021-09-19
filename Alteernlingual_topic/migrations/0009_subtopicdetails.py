# Generated by Django 3.2.5 on 2021-09-18 16:12

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Alteernlingual_topic', '0008_readcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTopicDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_explanations', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('AR_explanations', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('EN_explanations', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('FR_explanations', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('HA_explanations', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('IG_explanations', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('YO_explanations', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('published', models.DateField(auto_now_add=True, null=True)),
                ('language', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Alteernlingual_topic.language', verbose_name='language')),
                ('subtopic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Alteernlingual_topic.subtopic', verbose_name='subtopicdetail')),
            ],
        ),
    ]
