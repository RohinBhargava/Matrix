import math
from orthogonalization import *
from vec import *

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    return [x/math.sqrt(x * x) for x in orthogonalize(L) if x * x > 10E-14]


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    QStart, RStart = aug_orthogonalize(L)
    QList = orthonormalize(QStart)
    multiplier = list()
    j = 0
    for counter in range(len(QList)):
        if getitem(QList[counter],list(QList[0].D)[j]) == 0:
            if j < len(QList[0].D):
                j += 1
            else:
                j = 0
        x = (getitem(L[counter],list(L[0].D)[j]) - sum(multiplier[h] * getitem(RStart[counter],list(RStart[0].D)[h]) * getitem(QList[h],list(QList[0].D)[j]) for h in range(counter)))/(getitem(QList[counter],list(QList[0].D)[j]))
        if x > 10E-13:
            multiplier.append(x)
    RList = [Vec(RStart[i].D, { y : getitem(RStart[i],y) * multiplier[y] for y in range(len(multiplier))}) for i in range(len(RStart))]
    return (QList, RList)
