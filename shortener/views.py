from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortenedURL
import random
import string


# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        original_url = request.POST.get("url")
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        obj, created = ShortenedURL.objects.get_or_create(original_url=original_url, defaults={'short_url': short_url})
        context['short_url'] = request.build_absolute_uri('/') + obj.short_url
    return render(request, 'home.html', context)

def redirect_url(request, short_url):
    url_details = get_object_or_404(ShortenedURL, short_url=short_url)
    url_details.visits += 1
    url_details.save()
    return redirect(url_details.original_url)

def stats(request, short_url):
    url_details = get_object_or_404(ShortenedURL, short_url=short_url)
    return render(request, 'stats.html', {'url': url_details})