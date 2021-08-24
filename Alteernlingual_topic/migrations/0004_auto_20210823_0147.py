# Generated by Django 3.2.5 on 2021-08-23 00:47

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Alteernlingual_topic', '0003_auto_20210822_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='arabictopic',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='AR_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='frenchtopic',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='FR_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hausatopic',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='HA_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='igbotopic',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='IG_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='yorubatopic',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='YO_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='Arabic_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='arabictopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='English_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='englishtopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='French_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='frenchtopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='Hausa_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='hausatopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='Igbo_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='igbotopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='AR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='EN_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='FR_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='HA_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='IG_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='YO_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='Yoruba_title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='yorubatopic',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='YOReadCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='YO_posts', to='Alteernlingual_topic.yorubatopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IGReadCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IG_posts', to='Alteernlingual_topic.igbotopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HAReadCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HA_posts', to='Alteernlingual_topic.hausatopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FRReadCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FR_posts', to='Alteernlingual_topic.frenchtopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ARReadCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AR_posts', to='Alteernlingual_topic.arabictopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]