from django.shortcuts import render, redirect
from django.core.mail import send_mail

from homepage import forms
from homepage.models import AddProjects


def accueil(request):
    return render(request, "homepage/accueil.html")


def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=["calcagnoloic93@gmail.com"]
            )
            return redirect("email_send")
    else:
        form = forms.ContactForm()

    return render(request, "homepage/contact.html",
                  {'form': form})


def email_send(request):
    return render(request, "homepage/email_send.html")


def projet(request):
    projects = AddProjects.objects.order_by('-id')
    return render(request, "homepage/projets.html",
                  {'projects': projects})
