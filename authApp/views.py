from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate
# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        get_username =request.POST.get("username") 
        get_password = request.POST.get('password')
        user = authenticate(username = get_username, password=get_password)
        if user is not None:
            login(request, user)
            get_user = User.objects.get(id =user.id)
            messages.success(request, "Login successful")
            return redirect("urlShortenApp:homePage")
        else:
            messages.info(request, "user not recognized!")
            return redirect("authApp:loginPage")
            
    else:
        form = CustomAuthenticationForm()
        template_name = 'auth/loginForm.html'
        context = {
            'login_form':form
        }
        return render(request, template_name, context)
    

# logoutPage

def logoutPage(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("authApp:loginPage")


# registerPage
def registerPage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created")
            return redirect("authApp:loginPage")
        else:
            message.info(request, "Password missmatch Please try again")
            return redirect("authApp:registerPage")
    else:
        register_form = CustomUserCreationForm()
        template_name = 'auth/registration.html'
        context = {
            "register_form" :register_form
        }
        return render(request, template_name, context)