#Fixes

#Enhancements

- Create custom model representing selection tree/graph instead of generating Markov chain each time (can incorporate more books because of reduced time)
- NLTK instead of just Markov models to predict next word (include parts of speech)
- Better stripping of bad characters (and possibly reviews) from the descriptions
- Not ending on stop words? (still occasionally ending up with "A" at the end)
- Perhaps incorporate combination of NLTK (parts of speech) and Markov chains to determine successors