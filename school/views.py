from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


def health(request):
    return HttpResponse("ok")


@cache_page(60 * 5)
def home(request):
    return render(request, "school/home.html")


@cache_page(60 * 5)
def about(request):
    return render(request, "school/about.html")


@cache_page(60 * 5)
def curriculum(request):
    return render(request, "school/curriculum.html")


@cache_page(60 * 5)
def programs(request):
    return render(request, "school/programs.html")


@cache_page(60 * 5)
def contact(request):
    return render(request, "school/contact.html")
