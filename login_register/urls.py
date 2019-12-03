from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login_register'

urlpatterns = [
    path('profile/<int:pk>', views.ProfileView.as_view(), name = 'profile'),
    path('profile/current', views.CurrentProfileView.as_view(), name = 'current'),
    path('register/', views.register_view, name = 'register'),
    path('login/', views.LoginViewCus.as_view(redirect_authenticated_user=True,template_name="login_register/dangnhap.html"),name='login'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('reset_password/',views.ResetPasswordCustom.as_view(), name = 'reset'),
    path('reset_password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'login_register/reset_password_form.html',success_url='/users/login'), name='reset_confirm'),
    path('reset_password/done', auth_views.PasswordResetDoneView.as_view(template_name = 'login_register/reset_password.html'), name = 'reset_done'),
]