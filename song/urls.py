from django.urls import path
from .views.songView import index

urlpatterns = [
    path('', index, name='index'),
]
