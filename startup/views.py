from django.shortcuts import render,redirect
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form': form})

def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

@login_required(login_url='/accounts/login/')
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['dnnsmoyo@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

@login_required(login_url='/accounts/login/')
def successView(request):
    return HttpResponse('Success! Thank you for your message.')

@login_required(login_url='/accounts/login/')
def project(request):
    return render(request,'project.html')

@login_required(login_url='/accounts/login/')
def services(request):
    return render(request,'services.html')

def single_blog(request):
    return render(request,'single_blog.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")