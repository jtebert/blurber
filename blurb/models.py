from django.db import models
from utils import pkgen

# Create your models here.

class Genre(models.Model):
    id = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    # Have to pickle Markov objects before passing to constructor
    title_markov_chain = models.BinaryField()
    author_markov_chain = models.BinaryField()
    descr_markov_chain = models.BinaryField()

    def __unicode__(self):
        return self.name


class Blurb(models.Model):
    id = models.CharField(max_length=50, primary_key=True, default=pkgen)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    descr = models.TextField()
    genre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title

