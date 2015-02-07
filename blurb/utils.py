__author__ = 'mustafacamurcu'
from PyMarkovTextGenerator import Markov

def clean(data):
    """
    :param data: list of (title, author, blurb) tuples
    :return: tuple of Markov chains for (title, author, blurb)
    Strip HTML tags and parse each into Markov chain of appropriate depth
    """
    titles, authors, descriptions = zip(*data)

    for str in descriptions:
        b = 0
        i = 0
        for c in str:
            if c == '<' :
                b += 1
                str = str[:i] + str[i+1:]
                i -= 1
            elif c == '>':
                b -= 1
                str = str[:i] + str[i+1:]
                i -= 1
            elif b > 0:
                str = str[:i] + str[i+1:]
                i -= 1
            i += 1

    d_string = ""
    for str in descriptions:
        d_string = d_string + " " + str

    t_string = ""
    for str in titles:
        t_string = t_string + "\\" + str

    a_string = ""
    for str in authors:
        a_string = a_string + " " + str

    m1 = Markov(prob=True, level=1)
    m3 = Markov(prob=True, level=3)

    return (m1.parse(titles), m1.parse(authors), m3.parse(descriptions))


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