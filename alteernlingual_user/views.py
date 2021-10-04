from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# from alteernlingual_user.forms import SignUpForm
from django.contrib.auth.models import Group
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# from .forms import  UserForm, ProfileForm
from django.contrib import messages
from .forms import SignUpForm

from django.utils.decorators import method_decorator
from django.views import View

from .forms import ProfileForm, form_validation_error
from .models import Profile
from Alteernlingual_topic.models import SubTopic, LanguageFollow, Language
from alteernlingual_subjects.models import SubjectFollow
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def home(request):
        return render(request, 'index.html')

def topicPercent(read_count, total_topic):
    if total_topic == 0:
        total_topic = 1
    percentage = int(read_count / total_topic * 100)

    return percentage

@login_required
def dashboard(request):
    language_follow = LanguageFollow.objects.filter(user=request.user)
    read = LanguageFollow.objects.filter(user=request.user)
    read_count = SubTopic.objects.filter(read=request.user, language__language_follow__user=request.user).count()
    total_topic = SubTopic.objects.filter(language__language_follow__user=request.user).count()
    percent =  topicPercent(read_count, total_topic)
    subject_follow = SubjectFollow.objects.filter(user=request.user)
    last_read = SubTopic.objects.filter(read=request.user).last()

    return render(request, 'auth_user/userDashboard.html',  {
    "read_count": read_count, "total_topic": total_topic, 'language_follow': language_follow, "percent": percent,
    "subject_follow": subject_follow, "last_read": last_read

        })


def register_request(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get('email')
            htmly = get_template('registration/email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'a.damilare2012@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            user = authenticate(username=username, password=raw_password)
            user = form.save()
            login(request, user)

            msg = 'User created - please <a href="/accounts/login">login</a>.'
            success = True

            return redirect("profile")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form, "msg": msg, "success": success})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile, 'segment': 'profile'}
        return render(request, 'auth_user/userProfile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save()
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name = form.cleaned_data.get('last_name')
            profile.user.email = form.cleaned_data.get('email')
            profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('profile')


@login_required
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changePassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth_user/passwordChange.html', {
        'form': form
    })



def resetPassword(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password reset link has been sent to your email')
            return redirect('changePassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth_user/password_reset_form.html', {
        'form': form
    })


def termsOfService(request):
    return render(request, 'termsOfService.html')

def privacyPolicy(request):
    return render(request, 'privacyPolicy.html')

def partnerWithUS(request):
    return render(request, 'partnerWithUS.html')

def forEducators(request):
    return render(request, 'forEducators.html')

def forBusiness(request):
    return render(request, 'forBusiness.html')

def careers(request):
    return render(request, 'careers.html')

def ourApproach(request):
    return render(request, 'ourApproach.html')

def alteernlingualStory(request):
    return render(request, 'alteernlingualStory.html')

def blog(request):
    return render(request, 'blog.html')