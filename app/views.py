from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime


def home(request):
    return render(request, 'home.html', {
        'now': datetime.now().isoformat(),
    })


def health(request):
    return JsonResponse({'status': 'ok'})
