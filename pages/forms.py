from django import forms
from django.core.validators import EmailValidator
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"type": "email"}), validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)