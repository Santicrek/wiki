from django.shortcuts import render
from django.http import HttpResponse

from encyclopedia import util


# Create your views here.


def add(request):
    
    return render(request, "add/add.html", {
        "entries": util.list_entries()
    })