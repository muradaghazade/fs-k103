from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', home , name='home'),
    path('story/<int:id>/', story_detail , name='story_detail'),
]