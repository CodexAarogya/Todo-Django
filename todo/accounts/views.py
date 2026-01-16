from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
@login_required
def test_view(request,user_id):
    user = get_object_or_404(User,id=user_id)
    return render(request, 'base.html',{'user':user})

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.error(request,"Invalid Username!")
            return redirect(settings.LOGIN_URL)
        
        user = authenticate(request,username = username, password = password)
        if user is not None:
                login(request,user)
                return redirect(settings.LOGIN_REDIRECT_URL, user_id=user.id)
        else:
                messages.error(request, "Incorrect password!")
                return redirect(settings.LOGIN_URL)
    
    
    return render(request, 'registration/login.html')

def UserRegistration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

    # NEED TO IMPROVE THE EXCEPTION HANDLING IN BETTER WAY --- LATER -------
    # JUST HANDLING RANDOMLY FOR NOW ------
    # ------- MINOR BUGS --- ACCEPTING USERNAME AND PASSWORD WITH WHITESPACES---- NEED TO FIX LATER
        if User.objects.filter(username=username):
            messages.error(request,"Username already taken!")
            return redirect(settings.USER_REGISTRATION_URL)
        elif User.objects.filter(email=email):
            messages.error(request,"Email already taken!")
            return redirect(settings.USER_REGISTRATION_URL)
        
        elif not(password==confirm_password):
             messages.error(request,"Invalid Confirm password!")
             return redirect(settings.USER_REGISTRATION_URL)
        else:
    
            user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            return redirect(settings.LOGIN_URL)
    
    return render(request, 'registration/user_registration.html')

@login_required
def LogoutView(request):
     logout(request)
     return render(request, 'registration/logout.html')