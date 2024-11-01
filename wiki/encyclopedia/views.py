from django.shortcuts import render
from django.http import HttpResponse
import random

from . import util
from .util import get_entry


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def random_entry(request):
    entry_list = util.list_entries()  # Fetch entries list correctly
    random_title = random.choice(entry_list) if entry_list else None  # Pick a random entry if list is not empty
    random_entry = get_entry(random_title)

    return render(request, 'encyclopedia/random_entry.html', {
        "random_entry": random_entry,
    })