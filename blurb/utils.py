# -*- coding: utf-8 -*-
__author__ = 'mustafacamurcu'
from PyMarkovTextGenerator import Markov


def dehtml(str):
    """
    :param str: String to remove characters from
    :return: String w/out unnecessary characters
    Strip HTML tags from String
    """
    b = 0
    i = 0
    for c in str:
        if c == '(' :
            b += 1
            str = str[:i] + str[i+1:]
            i -= 1
        elif c == ')':
            b -= 1
            str = str[:i] + str[i+1:]
            i -= 1
        if c == '<' :
            b += 1
            str = str[:i] + str[i+1:]
            i -= 1
        elif c == '>':
            b -= 1
            str = str[:i] + str[i+1:]
            i -= 1
        elif c == '\\':
            b -= 1
            str = str[:i] + str[i+1:]
            i -= 1
        elif b > 0:
            str = str[:i] + str[i+1:]
            i -= 1
        elif c == '—':
            str = str[:i] + str[i+1:]
            i -= 1
        i += 1

    return str


def clean(data):
    """
    :param data: list of (title, author, blurb) tuples
    :return: tuple of Markov objects for (title, author, description)
    Strip HTML tags and append all strings (with break characters) per category
    """
    titles, authors, descriptions = zip(*data)

    t_string = ""
    for str in titles:
        t_string = t_string + str + "\\ "

    a_string = ""
    for str in authors:
        a_string = a_string + str + "\\ "

    d_string = ""
    for str in descriptions:
        d_string = d_string + " " + str

    #print "done cleaning"
    return (t_string, a_string, d_string)

def generate_title(m):
    """
    :param m: Markov object for title values
    :return: String of newly generated title
    """
    def end(s):
        interpunction = ("\\")
        if s[len(s)-1] in interpunction or len(s.split()) > 10:
            return True
        else:
            return False

    return dehtml(m.generate(endf=end))

def generate_description(m):
    """
    :param m: Markov object for description values
    :return: String of newly generated title
    """
    def end(s):
        interpunction = (".", "!", "?")
        if s[len(s)-1] in interpunction and len(s.split()) > 50:
            return True
        else:
            return False

    return dehtml(m.generate(endf=end))

def generate_author(m):
    """
    :param m: Markov object for author values
    :return: String of newly generated author
    """
    def end(s):
        interpunction = ('\\')
        if s[len(s)-1] in interpunction or len(s.split()) > 10:
            return True
        else:
            return False

    return dehtml(m.generate(endf=end))

def generate_all(strings):
    """
    :param strings: (all_titles, all_authors, all_descr)
    :return: (new_title, new_author, new_descr)
    Generate the random title/author/description using the Markov chains
    """
    m1 = Markov(prob=True, level=1)
    m2 = Markov(prob=True, level=1)
    m3 = Markov(prob=True, level=1)

    m1.parse(strings[0])
    m2.parse(strings[1])
    m3.parse(strings[2])

    t_string = kill_chars(generate_title(m1))
    a_string = kill_chars(generate_author(m2))
    d_string = kill_chars(generate_description(m3))

    t_string = generate_title(m1)
    a_string = generate_author(m2)
    d_string = generate_description(m3)

    t_list = t_string.split()
    while t_list[-1] in stop_words:
        t_list = t_list[0:-1]
    t_string = " ".join(t_list)

    return (t_string,a_string,d_string)


def generate_from_genre(genre):
    """
    :param genre: Genre model object
    :return: newly generated tuple (title, author, description) for the genre
    """
    # Get random strings for a given genre
    strs = (genre.title_options, genre.author_options, genre.descr_options)
    #print strs

    return generate_all(strs)


def get_all_genres():
    """
    :return: Dictionary for all genres of {genre_id, genre_name}
    Get all genre info from the database
    """
    from blurb.models import Genre
    genres = Genre.objects.all()
    genre_dict = {}
    for genre in genres:
        print genre_dict[genre.id]
        genre_dict[genre.id] = genre.name
    return genre_dict

def kill_chars(line):
    """
    :param str2: String
    :return: Cleaned String
    Removes specified characters from string (replaces with spaces)
    """

    invalid_characters = "[-—/\"”•\"“\']"
    for c in invalid_characters:
        line = line.replace(c,"")

    return line

def pkgen():
    """
    :return: alphanumeric primary key (String)
    Generate a random 6-digit primary key
    """
    from base64 import b32encode
    from hashlib import sha1
    from random import random
    rude = ('fuck', 'shit', 'damn', 'bitch', 'hell',)
    bad_pk = True
    while bad_pk:
        pk = b32encode(sha1(str(random())).digest()).lower()[:6]
        bad_pk = False
        for rw in rude:
            if pk.find(rw) >= 0: bad_pk = True
    return pk

stop_words_str = "a about above after again against all am an and any are aren't as at be because been before being below between " \
      "both but by can't cannot could couldn't did didn't do does doesn't doing don't down during each few for from " \
      "further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself " \
      "his how how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no " \
      "nor not of off on once only or other ought our ours ourselves out over own same shan't she she'd she'll she's " \
      "should shouldn't so some such than that that's the their theirs them themselves then there there's these they " \
      "they'd they'll they're they've this those through to too under until up very was wasn't we we'd we'll we're we've " \
      "were weren't what what's when when's where where's which while who who's whom why why's with won't would wouldn't " \
      "you you'd you'll you're you've your yours yourself yourselves"
stop_words = stop_words_str.split()