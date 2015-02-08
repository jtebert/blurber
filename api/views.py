from django.shortcuts import render
from blurb.models import Genre, Blurb
from django.shortcuts import get_object_or_404
import json
from django.http import HttpResponse
import blurb.utils as utils
from django.core import serializers
from django.http import JsonResponse


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
    genre = get_object_or_404(Genre, slug=slug)
    title, author, descr = utils.generate_from_genre(genre)
    genre_str = genre.name
    blurb_json = {
        'title': title,
        'author': author,
        'descr': descr,
        'genre_str': genre_str,
    }
    if will_save != 0:
        blurb_obj = Blurb(
            title = title,
            author = author,
            descr = descr,
            genre_str = genre_str
        )
        blurb_obj.save()
        blurb_json['permalink_pk'] = blurb_obj.id
        return JsonResponse(blurb_json)

def blurb_permalink(request, pk):
    blurb = get_object_or_404(Blurb, pk=pk)
    #return JsonResponse([blurb, ], safe=False)
    #return JsonResponse(serializers.serialize("json", [blurb,]), safe=False)
    return HttpResponse(serializers.serialize("json", [blurb,]))