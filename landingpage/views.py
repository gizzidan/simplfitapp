from django.shortcuts import render
from django.template import RequestContext

def index(request):
    return render(request, 'landingpage/index.html', {})
# Create your views here.
