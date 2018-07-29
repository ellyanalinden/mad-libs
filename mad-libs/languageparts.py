#!/usr/bin/env python

# import modules here
import random

# Create a dictionary of language parts. It must contain: noun, verb, adjective.
# The key should be one of the types of language (e.g. noun) and the value
# should be the list of words that you choose.
lang_parts = {
    'noun': ['man', 'mountain', 'state', 'ocean', 'country'],
    'verb': ['add', 'bite', 'work', 'run', 'arrest'],
    'adj' : ['ambitious', 'brave', 'calm', 'delightful', 'faithful']
}

# this is a function that you can learn about in the functions chapter
def get_word_part(part):
    # put your code to get a language part here
    #I am not sure how to code this part
    # get nouns
    noun = []
    random.shuffle(noun)
    # get adjective
    adj = []
    random.shuffle(adj)
    #get verb
    verb = []
    random.shuffle(verb)

    word = (noun[], adj[], verb[])
    # make sure that you return the language part e.g.
    return word
