from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from login_register.models import Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    re_email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta():
        model = User
        fields = ('username','email','re_email','password','re_password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            're_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            're_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': None,
            'email': None,
        }

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        re_email = all_clean_data['re_email']
        password = all_clean_data['password']
        re_password = all_clean_data['re_password']

        if email != re_email :
            raise forms.ValidationError("Email bạn nhập chưa đúng")

        if password != re_password :
            raise forms.ValidationError("Password bạn nhập chưa đúng")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone','pic')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean(self):
        all_clean_data = super().clean()
        phone = all_clean_data['phone']
        if (phone[0:3].lower() not in ['086','096','097','098','089','090','093','088','091','094','099','092','056','058'] and len(phone)==10)\
            and (phone[0:4].lower() not in ['0162','0163','0164','0165','0166','0167','0168','0169','0120','0121','0122','0126','0128','0123','0124','0125','0127','0129','0199'] and len(phone)==11):
            raise forms.ValidationError("Số điện thọai của bạn không hợp lệ, phải đăng ký bằng số diện thoại di động")

class UpdateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('password','re_password','first_name','last_name')
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            're_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        re_password = all_clean_data['re_password']

        if password != re_password :
            raise forms.ValidationError("Password bạn nhập chưa đúng")

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address','pic')
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
