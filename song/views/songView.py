from django.shortcuts import render
from ..models.song import Song
from random import choice

# from playsound import playsound
# playsound('audio.mp3'

def index(request):
	random_song = choice(Song.objects.all())
	context = {'random_song':random_song}

	return render(request, 'index.html', context)
