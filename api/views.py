from django.shortcuts import render
from blurb.models import Genre, Blurb
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponse
import blurb.utils as utils
from django.core import serializers
from django.http import JsonResponse


def docs(request):
    return render(request, "api/docs.html", {})


def genres(request):
    """
    List the slugs and names of all the available genres
    """
    genres = Genre.objects.all()
    vals = genres.values("slug", "name")
    slugs = map(lambda x: x['slug'], vals)
    names = map(lambda x: x['name'], vals)
    print slugs
    genre_dict = dict(zip(slugs, names))
    return JsonResponse(genre_dict)


def genre_blurb(request, slug, will_save):
    descr_length = int(request.GET.get('descr_length', 75))
    genre = get_object_or_404(Genre, slug=slug)
    title, author, descr = utils.generate_from_genre(genre, descr_length)
    genre_str = genre.name
    blurb_vals = {
        'title': title,
        'author': author,
        'descr': descr,
        'genre_str': genre_str,
    }
    blurb_json = {
                      'model': "blurb.blurb",
                      'fields': blurb_vals,
                  }
    if will_save != "0":
        blurb_obj = Blurb(
            title = title,
            author = author,
            descr = descr,
            genre_str = genre_str
        )
        blurb_obj.save()
        blurb_json['pk'] = blurb_obj.id
    return JsonResponse(blurb_json)

def blurb_permalink(request, pk):
    blurb = get_object_or_404(Blurb, pk=pk)
    #return JsonResponse([blurb, ], safe=False)
    #return JsonResponse(serializers.serialize("json", [blurb,]), safe=False)
    blurb_json = serializers.serialize("json", [blurb,])[1:-1]
    #return JsonResponse(blurb_json)
    return HttpResponse(blurb_json)