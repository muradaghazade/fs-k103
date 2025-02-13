from django.shortcuts import render
from core.models import Story, Category


def home(request):
    stories = Story.objects.order_by('-id')
    categories = Category.objects.all()
    new_story = stories.first()
    context = {
        'stories': stories,
        'new_story': new_story,
        'categories': categories
    }
    return render(request, 'index.html', context)
