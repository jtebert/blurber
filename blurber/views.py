from django.shortcuts import render
from blurb import utils
from blurb.models import Genre

# Create your views here.

def index(request):

    """
    genre_dict = utils.get_all_genres()
    sorted_genres = genre_dict.items()
    sorted_genres = sorted(sorted_genres, key=lambda x: x[1])
    """
    genres = Genre.objects.all()

    return render(
        request, 'blurber/index.html', {
            'genres': genres,
        }
    )

def about(request):
    return render(
        request, 'blurber/about.html', {}
    )