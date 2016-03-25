from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("This is the home page for Tutor Hunt")

def home(request):
    # Add anything that you want to add to the context
    context = {
        'k1': "latest_question_list",
    }
    
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render(context, request))

