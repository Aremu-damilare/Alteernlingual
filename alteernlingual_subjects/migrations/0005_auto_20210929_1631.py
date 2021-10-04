# Generated by Django 3.2.5 on 2021-09-29 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alteernlingual_subjects', '0004_rename_subjects_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='subject',
            name='language',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='AR_explanations',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='EN_explanations',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='FR_explanations',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='HA_explanations',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='IG_explanations',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='YO_explanations',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='language',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='main_explanations',
        ),
        migrations.AddField(
            model_name='topic',
            name='audio_file_ar',
            field=models.FileField(blank=True, default=None, null=True, upload_to='audios_en/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='audio_file_en',
            field=models.FileField(blank=True, default=None, null=True, upload_to='audios_en/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='audio_file_fr',
            field=models.FileField(blank=True, default=None, null=True, upload_to='audios_en/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='audio_file_ha',
            field=models.FileField(blank=True, default=None, null=True, upload_to='audios_en/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='audio_file_ig',
            field=models.FileField(blank=True, default=None, null=True, upload_to='audios_en/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='audio_file_yo',
            field=models.FileField(blank=True, default=None, null=True, upload_to='audios_en/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='audio_main_title',
            field=models.FileField(blank=True, default=None, null=True, upload_to='audios/'),
        ),
        migrations.AddField(
            model_name='topic',
            name='read',
            field=models.ManyToManyField(blank=True, related_name='readsubject', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='AR_title',
            field=models.TextField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='EN_title',
            field=models.TextField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='FR_title',
            field=models.TextField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='HA_title',
            field=models.TextField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='IG_title',
            field=models.TextField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='YO_title',
            field=models.TextField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='main_title',
            field=models.TextField(blank=True, default=None, max_length=50000, null=True),
        ),
        migrations.CreateModel(
            name='TopicContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=150, verbose_name='title')),
                ('main_explanations', models.TextField(blank=True, default=None, null=True)),
                ('audio_main', models.FileField(blank=True, default=None, null=True, upload_to='audios/')),
                ('AR_explanations', models.TextField(blank=True, default=None, null=True)),
                ('audio_file_ar', models.FileField(blank=True, default=None, null=True, upload_to='audios_ar/')),
                ('EN_explanations', models.TextField(blank=True, default=None, null=True)),
                ('audio_file_en', models.FileField(blank=True, default=None, null=True, upload_to='audios_en/')),
                ('FR_explanations', models.TextField(blank=True, default=None, null=True)),
                ('audio_file_fr', models.FileField(blank=True, default=None, null=True, upload_to='audios_fr/')),
                ('HA_explanations', models.TextField(blank=True, default=None, null=True)),
                ('audio_file_ha', models.FileField(blank=True, default=None, null=True, upload_to='audios_ha/')),
                ('IG_explanations', models.TextField(blank=True, default=None, null=True)),
                ('audio_file_ig', models.FileField(blank=True, default=None, null=True, upload_to='audios_ig/')),
                ('YO_explanations', models.TextField(blank=True, default=None, null=True)),
                ('audio_file_yo', models.FileField(blank=True, default=None, null=True, upload_to='audios_yo/')),
                ('published', models.DateField(auto_now_add=True, null=True)),
                ('subject', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alteernlingual_subjects.subject', verbose_name='language')),
                ('topic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alteernlingual_subjects.topic', verbose_name='topicdetail')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectSkillFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_skill_follow', to='alteernlingual_subjects.subjectskill', verbose_name='subject_skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='subjectskill',
            name='subject',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='alteernlingual_subjects.subject'),
        ),
        migrations.CreateModel(
            name='SubjectFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_follow', to='alteernlingual_subjects.subject', verbose_name='subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='skill',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='alteernlingual_subjects.subjectskill', verbose_name='subject_skill'),
        ),
    ]
