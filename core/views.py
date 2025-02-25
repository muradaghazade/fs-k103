from django.shortcuts import render, redirect
from core.models import *
from core.forms import *


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


def stories(request):
    search = request.GET.get('search')
    stories = Story.objects.order_by('-id')
    if search:
        stories = stories.filter(title__icontains=search)
    categories = Category.objects.all()
    context = {
        'stories': stories,
        'categories': categories,
    }
    return render(request, 'stories.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('salam')
            form.save()
            return redirect('core:home')
    form=ContactForm()
    return render(request, 'contact.html', {'form': form})