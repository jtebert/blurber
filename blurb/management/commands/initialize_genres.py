from django.core.management import BaseCommand
from django.utils.text import slugify
import blurb.amazon_api_for_books
import blurb.utils as utils
from blurb.models import Genre

class Command(BaseCommand):
    def handle(*args, **kwargs):
        print("I am running!")
        Genre.objects.all().delete()
        # Get the information from Amazon
        dict_books = blurb.amazon_api_for_books.getBooksFromAmazon()

        # Gather into strings for each genre
        genre_dict = {}
        for genre_id in dict_books:
            list_of_tuples = dict_books[genre_id]
            genre_dict[genre_id] = utils.clean(list_of_tuples)
        random_genre = blurb.amazon_api_for_books.getRandomBooks(dict_books)
        random_genre = utils.clean(random_genre)
        # Get genre names (need function)
        # Create Genre object and add to database
        genre_names_dict = blurb.amazon_api_for_books.getGenreId_GenreName(1000)

        for genre_id in genre_dict.keys():
            genre_temp = Genre(
                id = slugify(genre_names_dict[genre_id]),
                name = genre_names_dict[genre_id],
                title_options = genre_dict[genre_id][0],
                author_options =  genre_dict[genre_id][1],
                descr_options = genre_dict[genre_id][2],
            )
            genre_temp.save()
        random_genre = Genre(
            id=slugify('random'),
            name="Random",
            title_options = random_genre[0],
            author_options = random_genre[1],
            descr_options = random_genre[2],
        )
        random_genre.save()