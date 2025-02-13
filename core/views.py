from django.shortcuts import render
from core.models import Story, Category


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
