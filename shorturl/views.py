from django.shortcuts import render, redirect
from .form import UrlForm
import random, string
from .models import UrlModel, MainPage

def mainpage(request):
    form = MainPage.objects.all()
    context = {'form': form}
    return render(request, 'shorturl/mainpage.html', context)


def mainview(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            slug = "".join(random.choice(string.ascii_letters)for x in range(10))
            url = form .cleaned_data['url']
            new_url = UrlModel(url=url, slug=slug)
            new_url.save()
            return redirect('http://localhost:8000/shorturl/')
    else:
        form = UrlForm()
    urls = UrlModel.objects.all()
    context = {'form': form, 'urls': urls}
    return render(request, 'shorturl/mainurlpage.html', context)

