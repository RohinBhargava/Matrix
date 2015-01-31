from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0, len(review_options) - 1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """

    return_dictionary = dict()
    list = [ k for (i, k) in enumerate(strlist) ]
    
    for k in list:
        num = list.index(k)
        for z in k.split():
            if z not in return_dictionary.keys():
                return_dictionary[z] = {num}
            else:
                return_dictionary[z].add(num)

    return return_dictionary

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """

    list_adder = list()
    
    for z in query:
        if z in inverseIndex:
            list_adder.append(inverseIndex[z])

    return_set = list_adder[0]
    
    for u in list_adder:
        return_set =  return_set | u 
            
    return return_set

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """

    list_adder = list()

    for z in query:
        if z in inverseIndex:
            list_adder.append(inverseIndex[z])

    return_set = list_adder[0]
    
    for u in list_adder:
        return_set =  return_set & u 
                    
    return return_set
