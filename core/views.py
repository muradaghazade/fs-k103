from django.shortcuts import render
from core.models import Story


def home(request):
    stories = Story.objects.order_by('-id')
    context = {
        'stories': stories
    }
    return render(request, 'index.html', context)
