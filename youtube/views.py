from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse('Hello World from Youtube')
    return render(request, 'youtube/index.html')

def contact(request):
    # return HttpResponse('Hello World from Youtube')
    return render(request, 'youtube/contact.html')