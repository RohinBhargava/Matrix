# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from itertools import combinations
from independence import is_independent



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    randomVec = GF2vecGen(len(a0.D))
    if a0 * randomVec == s and b0 * randomVec == t:
        return randomVec
    return choose_secret_vector(s,t)
    


## Problem 2
# Give each vector as a Vec instance
'''
Rohin's note: There are multiple answers that work.
Use the following code in the shell to test your answer:
>>> from itertools import combinations
>>> from independence import is_independent
>>> vecs = [(secret_a0, secret_b0), (secret_a1, secret_b1), (secret_a2, secret_b2), (secret_a3, secret_b3), (secret_a4, secret_b4)]
>>> all(is_independent(list(sum(x,()))) for x in combinations(vecs,3))
If your output is True, you're done. Else you have to try again.
'''
secret_a0 = list2vec([one, one, 0, one, 0, one])
secret_b0 = list2vec([one, one, 0, 0, 0, one])
secret_a1 = list2vec([one, one, 0, 0, one, one])
secret_b1 = list2vec([0, one, 0, one, 0, one])
secret_a2 = list2vec([one, one, one, one, one, 0])
secret_b2 = list2vec([one, 0, one, 0, one, 0])
secret_a3 = list2vec([0, 0, one, 0, one, 0])
secret_b3 = list2vec([one, one, one, one, 0, 0])
secret_a4 = list2vec([one, one, one, one, 0, one])
secret_b4 = list2vec([one, 0, one, one, one, one])

def findVectors(listInput, numbers, bits, keys):
    if len(listInput) == numbers + 1:
        return listInput
    if len(listInput) < keys:
        while len(listInput) < keys:
            g = (GF2vecGen(bits), GF2vecGen(bits))
            listInput.append(g)
            if not all(is_independent(list(sum(x,()))) for x in combinations(listInput,len(listInput))):
                listInput.remove(g)
        return findVectors(listInput, numbers, bits, keys)
    c = (GF2vecGen(bits), GF2vecGen(bits))
    listInput.append(c)
    if not all(is_independent(list(sum(x,()))) for x in combinations(listInput,keys)):
        listInput.remove(c)
    return findVectors(listInput, numbers, bits, keys)
            
def GF2vecGen(bits):
    return list2vec(list(randGF2() for i in range(bits)))
