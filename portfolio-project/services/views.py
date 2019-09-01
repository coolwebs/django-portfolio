# This is the default way the views file is written when starting new app via command line
from django.shortcuts import render #can use this or the http method (but this is better I think)

# This is what the tutorial docs tell me to do (https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
# from django.http import HttpResponse

# Create your views here. (This was from lynda.com tutorial)
# def nick(request):
#     return render(request, 'services/home.html')

def index(request):
    # return HttpResponse("Hello, world. You're at the services index.")
    return render(request, 'services/home.html')