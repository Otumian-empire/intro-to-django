from django.shortcuts import render


# views
def home_page(request):
    return render(request, 'index.html', {'title': 'index page'})


def about_page(request):
    return render(request, 'about.html', {'title': 'about page'})


def contact_page(request):
    return render(request, 'contact.html', {'title': 'contact page'})


def temp_page(request):
    return render(request, 'hello.html', {'title': "hello Page"})
