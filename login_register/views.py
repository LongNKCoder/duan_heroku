from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordResetView
from django.http import HttpResponse
from login_register.models import Profile
from login_register.forms import ProfileForm,UserForm,UpdateProfileForm,UpdateUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,UpdateView
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from . import models
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage



class LoginViewCus(LoginView):
    def form_valid(self,form):
        return super().form_valid(form)

class ProfileView(DetailView):
    context_object_name = 'nguoidung'
    model = User
    template_name = 'login_register/current.html'
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['form_profile'] = UpdateProfileForm()
        context['form_user'] = UpdateUserForm()
        return context
    def post(self, request, *args, **kwargs):
        user_form = UpdateUserForm(data=request.POST)
        profile_form = UpdateProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = User.objects.get(pk=request.user.id)
            user.profile.address = profile_form.cleaned_data['address'] if profile_form.cleaned_data['address'] else user.profile.address
            profile = user.profile
            profile.pic = request.FILES['pic'] if request.FILES['pic'] else profile.pic
            user.first_name = user_form.cleaned_data['first_name'] if user_form.cleaned_data['first_name'] else user.first_name
            user.last_name = user_form.cleaned_data['last_name'] if user_form.cleaned_data['last_name'] else user.last_name
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile.save()
            return redirect('login_register:current')
        else:
            return HttpResponse('Password không đúng')


class CurrentProfileView(LoginRequiredMixin, ProfileView):
    context_object_name = 'nguoidung'
    def get_object(self):
        return self.request.user
    
def register_view(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'pic' in request.FILES:
                profile.pic = request.FILES['pic']
            profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('login_register/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            registered = True
            return render(request,'login_register/register_done.html',{'message':'Thank you for register we will redirect you in 5 seconds or you can click this link'})
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request,'login_register/dangky.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request,'login_register/register_done.html',{'message':'Thank you for your email confirmation. Now you can login your account.'})
    else:
        return HttpResponse('Activation link is invalid!')

class ResetPasswordCustom(PasswordResetView):
    template_name = 'login_register/reset_password.html'
    email_template_name='login_register/password_reset_email.html'
    success_url='/users/login'
    redirect_authenticated_user=True

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            confirm_email = form.cleaned_data['email']
            if not User.objects.filter(email=confirm_email):
                return render(request,'login_register/reset_password.html',{'message':'Email của bạn không có trong database vui lòng nhập lại','form':form})
            else:
                return super().form_valid(form)