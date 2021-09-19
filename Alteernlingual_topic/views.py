from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Language, LanguageFollow, Skill, SkillFollow, Topic, SubTopic, LanguageOfInteraction, LoiFollow, SubTopicDetails
from django.views.generic import TemplateView
from django.urls import reverse


class lessonsView(ListView):
    model = Skill
    context_object_name = 'posts'
    template_name = 'lessons/lessons.html'

    def get_queryset(self):
        return LanguageFollow.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = Language.objects.all()
        context['skill'] = Skill.objects.all()
        context['fcats'] = Skill.objects.filter(language__language_follow__user=self.request.user)
        context['cou'] = Topic.objects.filter(skill__skill_follow__user=self.request.user)
        context['follow_cats'] = LanguageFollow.objects.filter(user=self.request.user)
        context['follow_skill'] = SkillFollow.objects.filter(user=self.request.user)
        return context

class topicDetail(DetailView):
    model = Topic
    context_object_name = 'topic'
    template_name = 'lessons/lessons_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['subtopic'] = SubTopic.objects.filter(topic=self.get_object())
        return context

class subTopicDetail(DetailView):
    model = SubTopic
    context_object_name = 'topic'
    template_name = 'lessons/topic_detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['follow_cats'] = LoiFollow.objects.filter(loi__loi_follow__user=self.request.user)
        context['follow_lang'] = LanguageFollow.objects.filter(user=self.request.user)
        context['loi'] = LanguageOfInteraction.objects.all()
        context['topicdetails'] = SubTopicDetails.objects.filter(subtopic=self.get_object())
        return context


def readView(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    ENpost = get_object_or_404(SubTopic, slug=slug)
    red = False #past of read is red in this context not read
    if ENpost.read.filter(id=request.user.id).exists():
        ENpost.read.remove(request.user)
        red = False
    else:
        ENpost.read.add(request.user)
        red = True
    return redirect(request.META.get('HTTP_REFERER', ''))



class followLanguageView(TemplateView):
    template_name = 'lessons/lessons.html'

    def get(self, request, *args, **kwargs):
        language_id = kwargs['pk']
        language = Language.objects.filter(id=language_id).first()
        skill_id = kwargs['pk']
        skill = Skill.objects.filter(skill_follow__user=self.request.user).first()
        if language:
            if request.GET.get('unfollow'):
                LanguageFollow.objects.filter(language=language, user=self.request.user).delete()
                SkillFollow.objects.filter(skill=skill, user=self.request.user).delete()
                SubTopic.objects.filter(read=request.user).delete()
            elif LanguageFollow.objects.filter(language__language_follow__user=self.request.user).exists(): 
                LanguageFollow.objects.filter(language=language, user=self.request.user).delete()
            else:
                LanguageFollow.objects.get_or_create(language=language, user=self.request.user)

        return redirect(reverse('lessons'))



class FollowSkillView(TemplateView):
    template_name = 'lessons/lessons.html'

    def get(self, request, *args, **kwargs):
        skill_id = kwargs['pk']
        skill = Skill.objects.filter(id=skill_id).first()
        if skill:
            if request.GET.get('unfollow'):
                SkillFollow.objects.filter(skill=skill, user=self.request.user).delete()
            elif SkillFollow.objects.filter(skill__skill_follow__user=self.request.user).exists():
                SkillFollow.objects.filter(skill=skill, user=self.request.user).delete()
            else:
                SkillFollow.objects.get_or_create(skill=skill, user=self.request.user)

        return redirect(reverse('lessons'))



class FollowLoiView(TemplateView):
    template_name = 'blog/topicdetail.html'

    def get(self, request, *args, **kwargs):
        loi_id = kwargs['pk']
        loi = LanguageOfInteraction.objects.filter(id=loi_id).first()
        if loi:
            if request.GET.get('unfollow'):
                LoiFollow.objects.filter(loi=loi, user=self.request.user).delete()
            elif LoiFollow.objects.filter(loi__loi_follow__user=self.request.user).exists():
                LoiFollow.objects.filter(loi=loi, user=self.request.user).delete()
            else:
                LoiFollow.objects.get_or_create(loi=loi, user=self.request.user)

        return redirect(request.META.get('HTTP_REFERER', ''))

