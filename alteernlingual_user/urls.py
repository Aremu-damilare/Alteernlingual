from django.urls import path
from alteernlingual_user import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/dashboard', views.dashboard, name='dashboard'),
    path('accounts/profile', views.ProfileView.as_view(), name='profile'),
    path('accounts/change-password/', views.changePassword, name='passwordChange'),
  
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view
    	(template_name="auth_user/password_reset_form.html",
    	 email_template_name="auth_user/password_reset_email.html",
    	 subject_template_name="auth_user/password_reset_subject.txt"), name='password_reset'),

    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view
    	(template_name="auth_user/password_reset_done.html"), name='password_reset_done'),

    path('accounts/reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view
    	(template_name="auth_user/password_reset_confirm.html"), name='password_reset_confirm'),

    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view
    	(template_name="auth_user/password_reset_complete.html"), name='password_reset_complete'),

]

