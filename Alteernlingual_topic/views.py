from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from .models import EnglishTopic, IgboTopic, HausaTopic, YorubaTopic, FrenchTopic, ArabicTopic, Category

def Lessons(request):
    return render(request, 'lessons.html')

class CategoryList(ListView):
    model = Category
    context_object_name = 'Category'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'Category_detail.html'
    context_object_name = 'Category'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
      
        return context


class EnglishList(ListView):
    queryset = EnglishTopic.objects.all()
    template_name = 'lang_tutorials/EnglishTopic.html'
    paginate_by = 10
    context_object_name = 'EnglishTopic'

def ENReadView(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    ENpost = get_object_or_404(EnglishTopic, slug=slug)
    red = False #past of read is red in this context not read
    if ENpost.read.filter(id=request.user.id).exists():
        ENpost.read.remove(request.user)
        red = False
    else:
        ENpost.read.add(request.user)
        red = True
    return redirect(request.META.get('HTTP_REFERER', ''))


class IgboList(ListView):
    queryset = IgboTopic.objects.all()
    template_name = 'lang_tutorials/IgboTopic.html'
    paginate_by = 1
    context_object_name = 'IgboTopic'

def IGReadView(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    IGpost = get_object_or_404(IgboTopic, slug=slug)
    red = False #past of read is red in this context not read
    if IGpost.read.filter(id=request.user.id).exists():
        IGpost.read.remove(request.user)
        red = False
    else:
        IGpost.read.add(request.user)
        red = True
    return redirect(request.META.get('HTTP_REFERER', ''))


class HausaList(ListView):
    queryset = HausaTopic.objects.all()
    template_name = 'lang_tutorials/HausaTopic.html'
    paginate_by = 1
    context_object_name = 'HausaTopic'

def HAReadView(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    HApost = get_object_or_404(HausaTopic, slug=slug)
    red = False #past of read is red in this context not read
    if HApost.read.filter(id=request.user.id).exists():
        HApost.read.remove(request.user)
        red = False
    else:
        HApost.read.add(request.user)
        red = True
    return redirect(request.META.get('HTTP_REFERER', ''))


class YorubaList(ListView):
    queryset = YorubaTopic.objects.all()
    template_name = 'lang_tutorials/YorubaTopic.html'
    paginate_by = 7
    context_object_name = 'YorubaTopic'

def YOReadView(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    YOpost = get_object_or_404(YorubaTopic, slug=slug)
    red = False #past of read is red in this context not read
    if YOpost.read.filter(id=request.user.id).exists():
        YOpost.read.remove(request.user)
        red = False
    else:
        YOpost.read.add(request.user)
        red = True
    return redirect(request.META.get('HTTP_REFERER', ''))


class FrenchList(ListView):
    queryset = FrenchTopic.objects.all()
    template_name = 'lang_tutorials/FrenchTopic.html'
    paginate_by = 1
    context_object_name = 'FrenchTopic'

def FRReadView(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    FRpost = get_object_or_404(FrenchTopic, slug=slug)
    red = False #past of read is red in this context not read
    if FRpost.read.filter(id=request.user.id).exists():
        FRpost.read.remove(request.user)
        red = False
    else:
        FRpost.read.add(request.user)
        red = True
    return redirect(request.META.get('HTTP_REFERER', ''))


class ArabicList(ListView):
    queryset = ArabicTopic.objects.all()
    template_name = 'lang_tutorials/ArabicTopic.html'
    paginate_by = 1
    context_object_name = 'ArabicTopic'

def ARReadView(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    ARpost = get_object_or_404(ArabicTopic, slug=slug)
    red = False #past of read is red in this context not read
    if ARpost.read.filter(id=request.user.id).exists():
        ARpost.read.remove(request.user)
        red = False
    else:
        ARpost.read.add(request.user)
        red = True
    return redirect(request.META.get('HTTP_REFERER', ''))



class EnglishTopicDetailView(DetailView):
    model = EnglishTopic
    template_name = 'topics_details/EnglishTopic_detail.html'
    context_object_name = 'topic'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(EnglishTopicDetailView, self).get_context_data(**kwargs)
        return context

class IgboTopicDetailView(DetailView):
    model = IgboTopic
    template_name = 'topics_details/IgboTopic_detail.html'
    context_object_name = 'topic'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(IgboTopicDetailView, self).get_context_data(**kwargs)
        return context

class HausaTopicDetailView(DetailView):
    model = HausaTopic
    template_name = 'topics_details/HausaTopic_detail.html'
    context_object_name = 'topic'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(HausaTopicDetailView, self).get_context_data(**kwargs)
        return context

class YorubaTopicDetailView(DetailView):
    model = YorubaTopic
    template_name = 'topics_details/YorubaTopic_detail.html'
    context_object_name = 'topic'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(YorubaTopicDetailView, self).get_context_data(**kwargs)
        return context

class FrenchTopicDetailView(DetailView):
    model = FrenchTopic
    template_name = 'topics_details/FrenchTopic_detail.html'
    context_object_name = 'topic'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(FrenchTopicDetailView, self).get_context_data(**kwargs)
        return context

class ArabicTopicDetailView(DetailView):
    model = ArabicTopic
    template_name = 'topics_details/ArabicTopic_detail.html'
    context_object_name = 'topic'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ArabicTopicDetailView, self).get_context_data(**kwargs)
        return context

