from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse 
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Create your views here.
def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email)
        
        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your email is not verified.')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username= email, password= password)
        if user_obj:
            login(request, user_obj)
            messages.success(request, 'You are logged in successfully.')
            return HttpResponseRedirect('/')
        
        messages.warning(request, 'Invalid credentials.')
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'accounts/login.html')

def register_page(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email)
        
        if user_obj.exists():
            messages.warning(request, 'Email is already exist.')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = email
        )
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'An Email has been sent to your mail.')
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'accounts/register.html')

def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_varified = True
        user.save()
        return HttpResponseRedirect('/')
    except Exception as e:
        HttpResponse('Invalid email token.')