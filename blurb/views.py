from django.shortcuts import render
from django.shortcuts import get_object_or_404
from models import Genre, Blurb
from forms import *
import blurb.utils
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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

def genre_blurb(request, slug):
    print slug
    test = Genre.objects.all().values("slug")
    print test[0]['slug']
    print slug

    genre = get_object_or_404(Genre, slug=slug)
    title, author, descr = blurb.utils.generate_from_genre(genre)
    genre_str = genre.name

    if request.method == "POST":
        if "save_blurb" in request.POST:
            form = SaveBlurb(request.POST)
            if form.is_valid():
                new_blurb = form.save()
                print new_blurb
                blurb_key = new_blurb.id
                print blurb_key
                return HttpResponseRedirect(reverse("blurb:blurb_permalink", args=(blurb_key,)))
        else:
            return HttpResponseRedirect(reverse("blurb:genre_blurb",
                                                kwargs={'slug': genre.slug}))
    else:
        form = SaveBlurb(initial={
            'title': title,
            'author': author,
            'descr': descr,
            'genre_str': genre_str,
        })

    return render(
        request, 'blurb/blurb.html', {
            "title": title,
            "author": author,
            "descr": descr,
            "genre_str": genre_str,
            "form": form,
        }
    )

def blurb_permalink(request, pk):
    blurb = get_object_or_404(Blurb, pk=pk)
    return render(
        request, 'blurb/blurb.html', {
            "title": blurb.title,
            "author": blurb.author,
            "descr": blurb.descr,
            "genre_str": blurb.genre_str,
        }
    )