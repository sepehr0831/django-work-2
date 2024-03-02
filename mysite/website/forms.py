from django import forms
from website.models import Contact , Newsletter
from captcha.fields import CaptchaField

class Contactform(forms.ModelForm):
    #for captcha
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = "__all__"

class Newsform(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = "__all__"