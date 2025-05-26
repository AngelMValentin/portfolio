from django import forms
from django.core.validators import EmailValidator
from captcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"type": "email"}), validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()