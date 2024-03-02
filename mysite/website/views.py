from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from website.forms import Contactform , Newsform
from website.models import Contact , Newsletter
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request , "website/index.html",{})



def about(request):
    return render(request , "website/about.html",{})




def contact(request):
    form = Contactform()
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"your ticket submited successfully")
        else:
            messages.add_message(request,messages.ERROR,"your ticket didn't submited")

    return render(request , "website/contact.html",{"form":form})

def newsletter(request):
    if request.method == "POST":
        form = Newsform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
            return HttpResponseRedirect("/")

