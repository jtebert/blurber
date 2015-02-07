from django.shortcuts import render
from blurb import utils

# Create your views here.

def index(request):
    genre_dict = utils.get_all_genres()
    print genre_dict
    #genre_dict2 = {"25": genre_dict["25"]}
    #genre_dict = genre_dict2

    return render(
        request, 'blurber/index.html', {
            'genre_dict': genre_dict,
        }
    )

def about(request):
    return render(
        request, 'blurber/about.html', {}
    )