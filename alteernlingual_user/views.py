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

def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'auth_user/userDashboard.html')


def register_request(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            user = form.save()
            login(request, user)

            msg = 'User created - please <a href="/accounts/login">login</a>.'
            success = True

            return redirect("dashboard")

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

# def successView(request):
#     return HttpResponse('Success! Thank you.')

# Create your views here.
# @login_required

