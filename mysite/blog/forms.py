from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField



class Commentform(forms.ModelForm):
    #for captcha

    class Meta:
        model = Comment
        fields = ['post','name','email','subject','message']