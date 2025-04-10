from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def home_view(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            message_body = f"This is an email from your portfolio\nName: {name}\nEmail: {email}\nMessage:\n{message}"

            send_mail(
                "Email from Portfolio",
                message_body,
                email,
                ['angelvalentinusmc@gmail.com'],
                fail_silently=False,
            )

            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, "pages/index.html", {"form": form, "success": success})


