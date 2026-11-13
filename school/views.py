from django.http import HttpResponse
from django.shortcuts import render


def health(request):
    return HttpResponse("ok")


def home(request):
    return render(request, "school/home.html")


def about(request):
    return render(request, "school/about.html")


def curriculum(request):
    return render(request, "school/curriculum.html")


def programs(request):
    return render(request, "school/programs.html")


def contact(request):
    return render(request, "school/contact.html")
