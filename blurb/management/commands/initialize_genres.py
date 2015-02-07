from django.core.management import BaseCommand
import blurb.amazon_api_for_books
import blurb.utils as utils
class Command(BaseCommand):
    def handle(*args, **kwargs):
        print("I am running!")
        # Get the information from Amazon
        dict_books = blurb.amazon_api_for_books.getBooksFromAmazon()
        # Gather into strings for each genre
        genre_dict = {}
        for genre_id in dict_books:
            list_of_tuples = dict_books[genre_id]
            genre_dict[genre_id] = utils.clean(list_of_tuples)
        # Get genre names (need function)
        # Create Genre object and add to database
        def genre_names():
            names = {"23": "Sci-fi/Fantasy",
                     "12":"Romance" }

        blurb1 = utils.generate_all(genre_dict["25"])
        print blurb1[0] +"\n"
        print blurb1[1] + "\n"
        print blurb1[2] + "\n"