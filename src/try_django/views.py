from django.http import HttpResponse

from django.shortcuts import render


# views
def home_page(request):
    return HttpResponse("<h1>Home page</h1>")


def about_page(request):
    return HttpResponse("<h1>About page</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact page</h1>")


def temp_page(request):
    return render(request, 'hello.html', {'title': "Home Page"})
