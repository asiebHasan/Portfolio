from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .models import UserProfile, Service, Projects
from .forms import ContactForm
# Create your views here.


def home(request):
    user_profile = UserProfile.objects.first()
    services = Service.objects.all()
    return render(request, 'home/home.html', {
        'user_info': user_profile,
        'services': services
    })


def download_cv(request):
    user_profile = UserProfile.objects.first()
    if user_profile is not None:
        response = HttpResponse(
            user_profile.cv, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{user_profile.cv.name}"'

        return response
    else:
        raise Http404("No user profile records exist")


def services(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {
        'services': services
    })


def contact(request):
    user_profile = UserProfile.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = f"From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n{form.cleaned_data['message']}"
            from_email = form.cleaned_data['email']
            # Replace with your email address
            recipient_list = ['asieb.hasan.supto@gmail.com']

            # Send the email
            send_mail(subject, message, from_email,
                      recipient_list, fail_silently=False)

            # clearing form
            form = ContactForm()

            # Notify the user
            return render(request, 'contact/contact.html', {
                'user_info': user_profile,
                'form': form,
                'success': True
            })
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {
        'user_info': user_profile,
        'form': form,
        'success': False
    })


def professional_projects(request):
    category = 'professional'
    projects = Projects.objects.filter(category=category)
    return render(request, 'projects/projects.html', {
        'category': category,
        'projects': projects
    })


def personal_projects(request):
    category = 'personal'
    projects = Projects.objects.filter(category=category)
    return render(request, 'projects/projects.html', {
        'category': category,
        'projects': projects
    })


def project_detail(request, id, slug):
    project = get_object_or_404(Projects, id=id, slug=slug)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = f"From: {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n{form.cleaned_data['message']}"
            from_email = form.cleaned_data['email']
            # Replace with your email address
            recipient_list = ['asieb.hasan.supto@gmail.com']

            # Send the email
            send_mail(subject, message, from_email,
                      recipient_list, fail_silently=False)

            # clearing form
            form = ContactForm()

            # Notify the user
            return render(request, 'projects/details.html', {
                'project': project,
                'form': form,
                'success': True
            })
    else:
        form = ContactForm()
    return render(request, 'projects/details.html', {
        'project': project,
        'form': form,
        'success': False
    })
