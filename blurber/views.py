from django.shortcuts import render
from blurb import utils

# Create your views here.

def index(request):
    genre_dict = utils.get_all_genres()
    sorted_genres = genre_dict.items()
    sorted_genres = sorted(sorted_genres, key=lambda x: x[1])
    print sorted_genres

    return render(
        request, 'blurber/index.html', {
            'genres': sorted_genres,
        }
    )

def about(request):
    return render(
        request, 'blurber/about.html', {}
    )