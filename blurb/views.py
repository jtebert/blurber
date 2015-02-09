from django.shortcuts import render
from django.shortcuts import get_object_or_404
from models import Genre, Blurb
from forms import *
import blurb.utils
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse


def genre_blurb(request, slug):
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
            "show_permalinker": True,
        }
    )

def blurb_permalink(request, pk):
    try:
        blurb = get_object_or_404(Blurb, pk=pk)
    except:
        raise Http404("Blurb does not exist")

    if request.method == "POST" and "new_blurb" in request.POST:
        print "GOT HERE"
        genre = Genre.objects.get(name=blurb.genre_str)
        print genre
        print genre.slug
        return HttpResponseRedirect(reverse("blurb:genre_blurb",
                                            kwargs={'slug': genre.slug}))

    return render(
        request, 'blurb/blurb.html', {
            "title": blurb.title,
            "author": blurb.author,
            "descr": blurb.descr,
            "genre_str": blurb.genre_str,
            "show_permalinker": False,
        }
    )