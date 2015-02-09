# Testing out ways to use NLTK.

# Strip HTML tags with Django django.utils.html.strip_tags
# Use NLTK to tokenize/get types of words
# Part of speech tagging: http://streamhacker.com/2008/11/03/part-of-speech-tagging-with-nltk-part-1/
# POS prediction: http://www.inf.ed.ac.uk/teaching/courses/icl/nltk/probability.pdf (3.2.1)

"""
CURRENT = 2-word segment
ALL_POSSIBLE_NEXT = following possible words based on Markov chained (with type tags and probabilities)
NEXT_TYPE = type of word that will follow (Use NLTK to predict)
TYPE_POSSIBLE_NEXT = All those from ALL_POSSIBLE_NEXT that have type NEXT_TYPE (include probabilities)
NEXT = use probabilities to select a next word
CURRENT = CURRENT[1] + NEXT
"""