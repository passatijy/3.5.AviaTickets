import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'
    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    term = request.GET.get('term')
    key = 'search_query'
    timeout = 3
    #search_q = City.objects.all().filter(name__startswith=term)
    res = cache.get(key)
    results = []
    if res is None:
        res = City.objects.all().filter(name__startswith=term)
        cache.set(key, res, timeout)
    #print(search_q)
    for k in res:
        results.append(k.name)
    return JsonResponse(results, safe=False)
