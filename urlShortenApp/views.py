from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
import requests
from decouple import config


# Create your views here.
def homePage(request):
    if request.method == 'POST':
        get_url = request.POST.get('original_url')

        access_token =config('BITLY_ACCESS_TOKEN')  
        endpoint = "https://api-ssl.bitly.com/v4/shorten"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        data = {
            "long_url": get_url,
            "domain": "bit.ly"
        }
        
        response = requests.post(endpoint, json=data, headers=headers)
        
        if response.status_code == 200:
            form = UrlModelsForm(request.POST)
            shortened_url = response.json()['link']

            if form.is_valid():
                instance = form.save(commit = False)
                instance.shortened_url = shortened_url
                instance.save()
                messages.success(request, "url added successFull")
                print("url added successFull" )
                return redirect('urlShortenApp:homePage')

            else:
                messages.error(request, "form is not valid")
                print("form is not valid" )
                return redirect('urlShortenApp:homePage')

        else:
            
            messages.error(request, "shorten url not generated")
            print("shorten url not generated" )
            return redirect('urlShortenApp:homePage')

        # if form.is_valid():
        #     original_url = request.POST.get('original_url')

        #     # 9717f9f1978e69f7a5a1ac7f75b86f23f3e2fba6
            
        #     messages.success(request, "url added successFull")
        #     print("=============", get_url )
        #     return redirect('urlShortenApp:homePage')
    else:
        template_name = 'homePage/homePage.html'

        context= {

        }

        return render(request, template_name , context)















