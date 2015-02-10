# Blurber: a web app to make book blurbs.

###[Try it here](http://blurber.herokuapp.com/)

*This project was originally created at HackBeanpot 2015, where it was a finalist.*

People never seem to find time to read books anymore, or even read the blurbs on the book covers. We've created a solution by creating new book blurbs for all kinds of book genres. Select a genre to generate a random blurb, or take your chances with a blurb from everything under the sun (or everything on Amazon). If you find a one you like, you can create a permalink to share it or save it forever.

Built on the Amazon Product Advertising API and created with Markov Chains, you can now read about books that don't exist, so you don't have to feel guilty about not reading any more than the title and the first half of the blurb.

## Features

- Generate a book blurb with a title, author, and book description
- Choose a genre for your blurb or include all genres
- Save and share your favorite blurbs with permalink URLs
- API to create and save blurbs

## API

This simple API uses different URLs that return JSON files when called upon. This API can be used to see the available genres, create new blurs, and find blurbs you alraedy made. If you have any questions or trouble with the API, <a href="mailto:blurb@blurber.io">let us know</a>!

###Retrieve genres

`http://www.blurber.io/api/genres/`

Get the names and slugs of all available genres. (Random, incorporating books all genres, is considered a genre.) The slugs are used to specify the genre in the URL for creating blurbs.

###Create blurb

`http://www.blurber.io/api/GENRE_SLUG/SAVE/`
Use the slug of a genre (`GENRE_SLUG`) to generate a blurb. `SAVE` is a 1 or 0 telling whether or not to save a permalink to the blurb on the site. If saved, the JSON will include the key (`pk`) for the blurb.

<p>The optional parameter <span class="mono">descr_length</span></p> uses <span class="mono">NUM</span> as the minimum length of the blurb description. The description will end after the first sentence-ending punctuation after <span class="mono">NUM</span> words.

####Query Parameters

**`descr_length`** : specify the minimum number of words in the blurb description. The description will end after the the first sentence-ending punctution after this many words. (default = 75)

**`descr_depth`** : specify the depth of the Markov chain used to generate the description (1-4). Higher depth generally results in longer segments from a single source. For very short descriptions, use depth 1. (default = 1)

###Retrieve blurb

`http://www.blurber.io/api/p/PK`

Use the primary key `PK` of a blurb to retrieve the blurb.
