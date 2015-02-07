from django.shortcuts import render
from django.shortcuts import get_object_or_404
from models import Genre, Blurb
from forms import *

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

    # Create the Markov chain
    # parse
    # generate

    #utils.generate_all(utils.clean(list_of_tuples))


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

def temp_blurb(request):
    title = "This is a Title Test"
    author = "Author Nameses"
    descr = "Enim nesciunt in, cliche reprehenderit authentic selfies Intelligentsia irony ethical. American Apparel Godard fanny pack drinking vinegar selvage XOXO, ut Portland. Magna dolore cardigan slow-carb, fap High Life keytar skateboard lo-fi ugh Portland. Labore pork belly eu disrupt normcore placeat. Scenester vegan sunt, letterpress in vero commodo nesciunt locavore viral deep v PBR. Ugh PBR&B hashtag, small batch heirloom do asymmetrical farm-to-table forage XOXO minim street art Carles slow-carb distillery. Banjo next level High Life ut, lo-fi nulla consequat quis chillwave cred heirloom."
    genre = "fake genre"  # Turn genre object into string w/ str

    if request.method == "POST":
        form = SaveBlurb(request.post)
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