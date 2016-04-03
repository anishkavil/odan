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


def bootstraphome(request):
    cntxt = {
             'rndmTxt' : 'The quick brown fox jumps over the little lazy dog',
             }
    template = loader.get_template('main/indexbasic.html')
    return HttpResponse(template.render(cntxt,request))

def aboutus(request):
    cntxt = {
             'rndmTxt' : 'The quick brown fox jumps over the little lazy dog',
             }
    template = loader.get_template('main/aboutus.html')
    return HttpResponse(template.render(cntxt,request))

def contactus(request):
    cntxt = {
             'rndmTxt' : 'The quick brown fox jumps over the little lazy dog',
             }
    template = loader.get_template('main/contactus.html')
    return HttpResponse(template.render(cntxt,request))