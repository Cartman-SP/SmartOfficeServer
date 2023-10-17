from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from Server.models import *


def search(request):
    query = request.GET.get('q', '')
    results = User.objects.filter(Q(firstname__icontains=query) | Q(secondname__icontains=query)).values('firstname', 'secondname')[:10] 

    return JsonResponse(list(results), safe=False)

def main_page(request):
    return render(request, 'search.html')