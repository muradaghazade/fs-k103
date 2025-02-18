from django.shortcuts import render
from core.models import *


def home(request):
    stories = Story.objects.order_by('-id')
    categories = Category.objects.all()
    new_story = stories.first()
    holiday_stories = stories.filter(category__title='Holiday').order_by('-id')
    context = {
        'stories': stories,
        'new_story': new_story,
        'categories': categories,
        'holiday_stories': holiday_stories
    }
    return render(request, 'index.html', context)


def story_detail(request, id):
    story = Story.objects.get(id=id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_stories = Story.objects.order_by('-id')[:3]
    context = {
        'story': story,
        'categories': categories,
        'tags': tags,
        'recent_stories': recent_stories,
    }
    return render(request, 'single.html', context)