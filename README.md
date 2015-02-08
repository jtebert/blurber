# Blurber: a web app for book blurbs.

###[Try it here](http://blurber.herokuapp.com/)

People never seem to find time to read books anymore, or even read the blurbs on the book covers. We've created a solution by creating new book blurbs for all kinds of book genres. Select a genre to generate a random blurb, or take your chances with a blurb from everything under the sun (or everything on Amazon). If you find a one you like, you can create a permalink to share it or save it forever.

Built on the Amazon Product Advertising API and created with Markov Chains, you can now read about books that don't exist, so you don't have to feel guilty about not reading any more than the title and the first half of the blurb.

## Features

- Generate a book blurb with a title, author, and book description
- Choose a genre for your blurb or include all genres
- Save and share your favorite blurbs with permalink URLs
- API to create and save blurbs

## API

`http://blurber.herokuapp.com/api/genres/`

Get the names and slugs of all available genres. (Random, incorporating all genres, is considered a genre.)

`http://blurber.herokuapp.com/api/<genre_slug>/<save>/`

Use the slug of a genre to generate a blurb. `<save>` is a 1 or 0 telling whether or not to save a permalink to the blurb on the site.

`http://blurber.herokuapp.com/api/p/<pk>`

Use the primary key <pk> of a blurb to retrieve the blurb.
