from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from main.forms import ContactForm

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
    values = request.META.items()
    values.sort()
    htmldata=[]
    for k,v in values:
         htmldata.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
         
    
    if request.method =='GET':
        form = ContactForm()
        return render(request, 'main/contactus.html', {'form': form,'htmldata':htmldata})
    else :
        form = ContactForm(request.POST)
        cntxt = {
             'rndmTxt' : 'The quick brown fox jumps over the little lazy dog',
             }
        template = loader.get_template('main/contactus.html')
        return HttpResponse(template.render(cntxt,request))