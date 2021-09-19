from django.shortcuts import render
from Alteernlingual_topic.models import Language
from .models import Subject, Topic
from django.views.generic import ListView, DetailView

class subjectView(ListView):
    model = Language
    context_object_name = 'languages'
    template_name = 'subjects/listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class languageDetail(DetailView):
    model = Language
    context_object_name = 'subjects'
    template_name = 'subjects/subjectdetail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['subjects'] = Subject.objects.filter(language=self.get_object())
        return context


class subjectDetail(DetailView):
    model = Subject
    context_object_name = 'subject'
    template_name = 'subjects/subject_topic_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['topics'] = Topic.objects.filter(subject=self.get_object())
        return context


class topicDetail(DetailView):
    model = Topic
    context_object_name = 'topic'
    template_name = 'subjects/subject_topic_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context