from django.shortcuts import render


def home(request):

    return render(request, "home.html")


def about_me(request):


    return render(request, "single_pages/about_me.html")