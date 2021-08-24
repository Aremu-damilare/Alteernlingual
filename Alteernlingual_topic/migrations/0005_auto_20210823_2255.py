# Generated by Django 3.2.5 on 2021-08-23 21:55

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Alteernlingual_topic', '0004_auto_20210823_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='arabictopic',
            name='title',
            field=models.CharField(default=datetime.datetime(2021, 8, 23, 21, 54, 52, 682041, tzinfo=utc), max_length=75, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='englishtopic',
            name='title',
            field=models.CharField(default=datetime.datetime(2021, 8, 23, 21, 55, 0, 183805, tzinfo=utc), max_length=75, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='frenchtopic',
            name='title',
            field=models.CharField(default=datetime.datetime(2021, 8, 23, 21, 55, 4, 206085, tzinfo=utc), max_length=75, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hausatopic',
            name='title',
            field=models.CharField(default=datetime.datetime(2021, 8, 23, 21, 55, 6, 586250, tzinfo=utc), max_length=75, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='igbotopic',
            name='title',
            field=models.CharField(default=datetime.datetime(2021, 8, 23, 21, 55, 8, 897632, tzinfo=utc), max_length=75, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='yorubatopic',
            name='title',
            field=models.CharField(default=datetime.datetime(2021, 8, 23, 21, 55, 11, 179791, tzinfo=utc), max_length=75, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='Arabic_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=50000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='English_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=50000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='French_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=50000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='Hausa_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=50000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='Igbo_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=50000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='Yoruba_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=50000, null=True, unique=True),
        ),
    ]
