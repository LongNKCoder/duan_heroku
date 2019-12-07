from django import forms
from django.core import validators
from .models import  Post,Image,ReportPost

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['state','create_date','update_date','user']

class ImageForm(forms.ModelForm):
    pic = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}))
    class Meta:
        model = Image
        fields = ('pic',)

class PostFormUpdate(forms.ModelForm):
    state = forms.ChoiceField(label="State",
                                choices=[('open','Mở'),('close','Đóng')],
                                widget=forms.Select(),
                                required=False)
    class Meta:
        model = Post
        fields = ['state','title','price','content']

class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportPost
        fields = ['post','pic','content','type_report']
        widgets = {'post': forms.HiddenInput()}