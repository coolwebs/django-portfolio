# This is the default way the views file is written when starting new app via command line
from django.shortcuts import render #can use this or the http method (but this is better I think)
from .models import Service

# This is what the tutorial docs tell me to do (https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
# from django.http import HttpResponse

# Create your views here
def index(request):
    services = Service.objects
    return render(request, 'services/home.html', {'services': services})