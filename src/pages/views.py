from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("Hello World")
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    # return HttpResponse("Hello World")
    my_context = {
        "text": "this is about me",
        "list": ['item1', 'item2', 'item3']
    }
    return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
    # return HttpResponse("Hello World")
    return render(request, "contact.html", {})
