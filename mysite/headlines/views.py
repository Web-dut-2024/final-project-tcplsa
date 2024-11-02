from django.shortcuts import render,redirect
from django.core.files.storage import default_storage
import random
from django.db.models import Q
import re
from django.core.files.base import ContentFile
from . import util


# Create your views here.

def home(request):
    return render(request, "headlines/home.html", {
        "entries": util.list_entries_with_urls()
    })

def CSDN(request):
    return render(request, "headlines/CSDN.html", {
        "entries": util.list_entries_with_urls_CSDN()
    })

def GIT(request):
    return render(request, "headlines/GIT.html", {
        "entries": util.list_entries_with_urls_GIT()
    })


def random_page(request):
    entries=util.list_entries_with_urls()
    if entries:
        random_entry = random.choice(entries)
        print(random_entry["url"])
        return redirect(random_entry["url"])


def search(request):
    
    query = request.GET.get('q', '').strip()
    if query:
        answer=util.list_entries_with_urls_search(query)
        if answer:
            return render(request, "headlines/Search.html", {
                "entries": util.list_entries_with_urls_search(query)
            })
        else:
            return render(request, 'headlines/404.html', status=404)
    else:
        # If the query is empty, redirect to the index page
        return redirect('CSDN')