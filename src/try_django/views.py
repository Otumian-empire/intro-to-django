from django.shortcuts import render

# import form
from .forms import ContactForm


# views
def home_page(request):
    return render(request, 'index.html', {'title': 'index page'})


def about_page(request):
    return render(request, 'about.html', {'title': 'about page'})


def contact_page(request):
    # print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        'title': 'contact page',
        'form': form
    }

    return render(request, 'form.html', context=context)


def temp_page(request):
    return render(request, 'hello.html', {'title': "hello Page"})
