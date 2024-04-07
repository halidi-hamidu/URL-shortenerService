from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
import requests
from decouple import config
from django.contrib.auth.models import User


# Create your views here.
@login_required
def homePage(request):
    if request.method == 'POST':
        get_url = request.POST.get('original_url')
        # access_token =config('BITLY_ACCESS_TOKEN')  
        access_token ='9717f9f1978e69f7a5a1ac7f75b86f23f3e2fba6'  
        endpoint = "https://api-ssl.bitly.com/v4/shorten"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        data = {
            "long_url": get_url,
            # "domain": "bit.ly"
        }
        
        response = requests.post(endpoint, json=data, headers=headers)
        
        if response.status_code == 200:
            form = UrlModelsForm(request.POST)
            shortened_url = response.json()['link']
            if form.is_valid():
                instance = form.save(commit = False)
                instance.shortened_url = shortened_url
                instance.created_by = request.user
                instance.save()
                messages.success(request, "url added successFull")
                print("url added successFull" )
                return redirect('urlShortenApp:urlListPage')
            else:
                messages.error(request, "form is not valid")
                print("form is not valid" )
                return redirect('urlShortenApp:homePage')
        else:
            messages.error(request, "shorten url not generated")
            print("shorten url not generated" )
            return redirect('urlShortenApp:homePage')
    else:
        template_name = 'homePage/homePage.html'

        context= {

        }

        return render(request, template_name , context)


# urlListPage
@login_required
def urlListPage(request):
    get_all_original_urls_and_shorten_url_generated_by_user = UrlModels.objects.filter(created_by = request.user)
    template_name = 'homePage/urlListPage.html'
    context  ={
        'get_all_original_urls_and_shorten_url_generated_by_user':get_all_original_urls_and_shorten_url_generated_by_user
    }

    return render(request, template_name, context)
    












