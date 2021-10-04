from django.shortcuts import render, get_object_or_404, redirect
from Alteernlingual_topic.models import Language
from .models import Subject, Topic, SubjectSkill, SubjectFollow, SubjectSkillFollow, TopicContent
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class subjectView(ListView):
    model = Subject
    context_object_name = 'subjects'
    template_name = 'subjects/listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        context['subjectskill'] = SubjectSkill.objects.all()
        context['fsubject'] = SubjectSkill.objects.filter(subject__subject_follow__user=self.request.user)
        # context['cou'] = Topic.objects.filter(skill__skill_follow__user=self.request.user)
        # context['follow_cats'] = LanguageFollow.objects.filter(user=self.request.user)
        # context['follow_skill'] = SkillFollow.objects.filter(user=self.request.user)
        return context

class followSubjectView(TemplateView):
    template_name = 'subjects/listview.html'

    def get(self, request, *args, **kwargs):
        subject_id = kwargs['pk']
        subject = Subject.objects.filter(id=subject_id).first()
        skill_id = kwargs['pk']
        skill = SubjectSkill.objects.filter(subject_skill_follow__user=self.request.user).first()
        if subject:
            if request.GET.get('unfollow'):
                SubjectFollow.objects.filter(subject=subject, user=self.request.user).delete()
                SubjectSkillFollow.objects.filter(skill=skill, user=self.request.user).delete()
            elif SubjectFollow.objects.filter(subject__subject_follow__user=self.request.user).exists(): 
                SubjectFollow.objects.filter(subject=subject, user=self.request.user).delete()
            else:
                SubjectFollow.objects.get_or_create(subject=subject, user=self.request.user)

        return redirect(reverse('subject:subject_view'))


class followSkillView(TemplateView):
    template_name = 'subjects/listview.html'

    def get(self, request, *args, **kwargs):
        subject_id = kwargs['pk']
        subject = Subject.objects.filter(id=subject_id).first()
        skill_id = kwargs['pk']
        skill = SubjectSkill.objects.filter(subject_skill_follow__user=self.request.user).first()
        if subject:
            if request.GET.get('unfollow'):
                SubjectFollow.objects.filter(subject=subject, user=self.request.user).delete()
                SubjectSkillFollow.objects.filter(skill=skill, user=self.request.user).delete()
            elif SubjectFollow.objects.filter(subject__subject_follow__user=self.request.user).exists(): 
                SubjectFollow.objects.filter(subject=subject, user=self.request.user).delete()
            else:
                SubjectFollow.objects.get_or_create(subject=subject, user=self.request.user)

        return redirect(reverse('subject:subject_view'))


class subjectDetail(DetailView):
    model = SubjectSkill
    context_object_name = 'topic'
    template_name = 'subjects/subject_skill_detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['topics'] = Topic.objects.filter(skill=self.get_object())
        return context


class topicContentDetail(DetailView):
    model = Topic
    context_object_name = 'topictitle'
    template_name = 'subjects/subject_topic_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['topiccontent'] = TopicContent.objects.filter(topic=self.get_object())
        return context