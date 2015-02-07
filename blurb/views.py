from django.shortcuts import render
from django.shortcuts import get_object_or_404
from models import Genre, Blurb

# Create your views here.

def random_blurb(request):
    genre = Genre.objects.order_by('?')[0]
    # Randomly select genre
    # Then the same as genre_blurb
    title = ""  # TODO: Fill these in from Markov results
    author = ""
    descr = ""
    return render(
        request, 'blurb/blurb.html', {
            "title": title,
            "author": author,
            "descr": descr,
        }
    )

def genre_blurb(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    # Use the genre's markov field to generate the book title, author, and blurb
    title = "" # TODO: Fill these in from Markov results
    author = ""
    descr = ""
    return render(
        request, 'blurb/blurb.html', {
            "title": title,
            "author": author,
            "descr": descr,
        }
    )

def blurb_permalink(request, pk):
    blurb = get_object_or_404(Blurb, pk=pk)
    title = ""  # TODO: Fill these in from correct Blurb
    author = ""
    descr = ""
    return render(
        request, 'blurb/blurb.html', {
            "title": title,
            "author": author,
            "descr": descr,
        }
    )