from typing import List
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
from .models import Language, LanguageFollow, LanguageLevel, LevelFollow, LanguageOfInteraction, LoiFollow, Topic
from django.views.generic import TemplateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import SubTopicDetailForm
from django.http import HttpResponse, HttpResponseRedirect

@method_decorator(login_required(), 'dispatch')
class lessonsView(ListView):
    model = Topic
    context_object_name = 'posts'
    template_name = 'lessons/lessons.html'
    paginate_by = 10

    def get_queryset(self):
        return Topic.objects.filter(level__level_follow__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['language'] = Language.objects.all()
        context['level'] = LanguageLevel.objects.all()
        context['fcats'] = LanguageLevel.objects.filter(language__language_follow__user=self.request.user)
        context['cou'] = Topic.objects.filter(level__level_follow__user=self.request.user)
        context['follow_cats'] = LanguageFollow.objects.filter(user=self.request.user)
        # context['follow_level'] = LanguageLevel.objects.filter(user=self.request.user)
        context['if_follow'] = LanguageFollow.objects.filter(language__language_follow__user=self.request.user).exists()
        # context['if_skill'] = LanguageLevel.objects.filter(level__level_follow__user=self.request.user).exists()
        return context

@method_decorator(login_required(), 'dispatch')
class TopicList(ListView):
    model = Topic
    context_object_name = 'topic'
    template_name = 'lessons/lessons.html'
    

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['subtopic'] = Topic.objects.filter(level__level_follow__user=self.request.user)
        return context

        
@method_decorator(login_required(), 'dispatch')
class TopicDetail(DetailView):
    model = Topic
    context_object_name = 'topic'
    template_name = 'lessons/topic_detail.html'
    slug_field = 'slug'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['follow_cats'] = LoiFollow.objects.filter(user=self.request.user)
        context['follow_lang'] = LanguageFollow.objects.filter(user=self.request.user)
        context['loi'] = LanguageOfInteraction.objects.all()
        # context['topicdetails'] = Topic.objects.filter(level=self.get_object())
        # context['prev_topic'] = SubTopicDetails.objects.filter(subtopic=self.get_object()).last()
        # context['form'] = SubTopicDetailForm()
        context['follow_loi'] = LoiFollow.objects.filter(loi__loi_follow__user=self.request.user).exists()
        return context


# def CommentCreateView(request, pk):
#     form = SubTopicDetailForm(request.POST or None)

#     if request.method == 'POST':
#         form = SubTopicDetailForm(request.POST, request.FILES)
#         if form.is_valid() and pk:
#             form.instance.user = request.user
#             form.instance.request = SubTopic.objects.get(pk=pk)

#             title = request.POST.get("title")
#             main_explanations = request.POST.get("main_explanations")
#             audio_main = request.FILES.get("audio_main")

#             form = SubTopicDetails(subtopic=form.instance.request,  title=title, main_explanations=main_explanations, audio_main=audio_main)
#             form.save()
#             return HttpResponseRedirect(reverse('topic_detail', kwargs={'pk': pk}))
#     return HttpResponseRedirect(reverse('topic_detail', kwargs={'pk': pk}))


def readView(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    ENpost = get_object_or_404(Topic, slug=slug)
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
        level_id = kwargs['pk']
        level = LanguageLevel.objects.filter(level_follow__user=self.request.user).first()
        if language:
            if request.GET.get('unfollow'):
                LanguageFollow.objects.filter(language=language, user=self.request.user).delete()
                LevelFollow.objects.filter(level=level, user=self.request.user).delete()
            elif LanguageFollow.objects.filter(language__language_follow__user=self.request.user).exists(): 
                LanguageFollow.objects.filter(language=language, user=self.request.user).delete()
            else:
                LanguageFollow.objects.get_or_create(language=language, user=self.request.user)

        return redirect(reverse('lessons'))



class FollowlevelView(TemplateView):
    template_name = 'lessons/lessons.html'

    def get(self, request, *args, **kwargs):
        level_id = kwargs['pk']
        level = LanguageLevel.objects.filter(id=level_id).first()
        if level:
            if request.GET.get('unfollow'):
                LevelFollow.objects.filter(level=level, user=self.request.user).delete()
            elif LevelFollow.objects.filter(level__level_follow__user=self.request.user).exists():
                LevelFollow.objects.filter(level=level, user=self.request.user).delete()
            else:
                LevelFollow.objects.get_or_create(level=level, user=self.request.user)

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


        

# Define function to search book
from django.db.models import Q
def search(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Topic.objects.filter(main_explanations__contains=query_name )
            return render(request, 'lessons/search.html', {"results":results, "query_name":query_name},)

    return render(request, 'lessons/search.html')

