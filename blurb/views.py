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

def genre_blurb(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    title, author, descr = blurb.utils.generate_from_genre(genre)
    genre_str = genre.name

    print "I AM HERE"

    if request.method == "POST":
        if "save_blurb" in request.POST:
            print "FOUND POST"
            form = SaveBlurb(request.POST)
            if form.is_valid():
                print "FORM VALID"
                new_blurb = form.save()
                print new_blurb
                blurb_key = new_blurb.id
                print blurb_key
                return HttpResponseRedirect(reverse("blurb:blurb_permalink", args=(blurb_key,)))
            else:
                print "INVALID FORM"
        else:
            return HttpResponseRedirect(reverse("blurb:genre_blurb", args=(pk,)))
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
    title = ""  # TODO: Fill these in from correct Blurb
    author = ""
    descr = ""
    genre_str = ""
    return render(
        request, 'blurb/blurb.html', {
            "title": title,
            "author": author,
            "descr": descr,
            "genre_str": genre_str,
        }
    )

def temp_blurb(request):
    title = "This is a Title Test"
    author = "Author Nameses"
    descr = "Enim nesciunt in, cliche reprehenderit authentic selfies Intelligentsia irony ethical. American Apparel Godard fanny pack drinking vinegar selvage XOXO, ut Portland. Magna dolore cardigan slow-carb, fap High Life keytar skateboard lo-fi ugh Portland. Labore pork belly eu disrupt normcore placeat. Scenester vegan sunt, letterpress in vero commodo nesciunt locavore viral deep v PBR. Ugh PBR&B hashtag, small batch heirloom do asymmetrical farm-to-table forage XOXO minim street art Carles slow-carb distillery. Banjo next level High Life ut, lo-fi nulla consequat quis chillwave cred heirloom."
    genre = "fake genre"  # Turn genre object into string w/ str

    if request.method == "POST":
        form = SaveBlurb(request.POST)
        if form.is_valid():
            # Process and save
            pass
    else:
        form = SaveBlurb(initial={
            'title': title,
            'author': author,
            'descr': descr,
            'genre': genre
        })

    return render(
        request, 'blurb/blurb.html', {
            "title": title,
            "author": author,
            "descr": descr,
            "genre": genre,
            'form': form
        }
    )