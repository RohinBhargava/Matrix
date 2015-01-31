# Please fill out this stencil and submit using the provided submission script.

## Problem 1
def myFilter(L, num):

    return_list = list()
    
    for u in L:
        if u % num != 0:
            return_list.append(u)

    return return_list

## Problem 2
def myLists(L):

    return_list = list()

    for u in L:
        return_list.append([i + 1 for i in range(u)])

    return return_list

## Problem 3
def myFunctionComposition(f, g):

    return_dict = dict()
    
    for k, i in f.items():
        if i in g.keys():
            return_dict[k] = g[i]

    return return_dict


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j
complex_addition_b = 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = 0.001 + 9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    return_sum = 0
    
    for u in L:
        return_sum = return_sum + u
        
    return return_sum

## Problem 7
def myProduct(L):
    product = 1

    for u in L:
        product = product * u

    return product


## Problem 8
def myMin(L):
    minimum = L[0]
    
    for u in L:
        if u <= minimum:
            minimum = u

    return minimum

## Problem 9
def myConcat(L):
    return_string = ''

    for u in L:
        return_string = return_string + u

    return return_string

## Problem 10
def myUnion(L):
    returner_set = set()
    
    for u in L:
        returner_set = returner_set | u

    return returner_set
