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
    # NOTE: use  'part' (which is going to be either 'noun', 'verb', or
    # 'adjective') to get the type of words from your 'lang_parts' dictionary.
    # Store the result in a variable called 'words'
    part = lang_parts.keys()
    return part
    words = get_word_part(part)

    # NOTE: you can use 'random.shuffle(words)' to mix up 'words' and then just
    # grab the first element or you can use 'random.choice(words)' to select a
    # random element. You could also use random.randint(0, len(words)-1) to get
    # a random index and then use that index to select a word. Store the result
    # of this operation in a variable called word
    word = random.choice(list(d.items()))
    # NOTE: once you have a word you just say 'return word' and that's it! (so
    # you don't need to change anything here).
    return word


    # make sure that you return the language part e.g.
    return word
