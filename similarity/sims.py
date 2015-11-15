"""
PUGS set similarity modules

Ethan Lew
11/10/15
"""
from math import*
from decimal import Decimal

def norm(x):
    """
    Determines the normal of a vector, if a vector doesn't have one (a zero vector), it returns None
    """
    if x is None:
        return None
    else:
        return round(sqrt(sum([a*a for a in x])),3)

def nth_root(value, n_root):
    try:
        root_value = 1/float(n_root)
        return round (Decimal(value) ** Decimal(root_value),3)
    except ZeroDivisionError:
        return None

def unit(x):
    """
    Scales a vector to unit length
    """
    x_len = norm(x)
    if x_len is None or x_len == 0:
        return None
    else:
        return[round(a/x_len, 3) for a in x]

def cosine(x,y):
    """
    Determines cos(theta) of two vectors
    """
    try:
        numerator = sum(a*b for a,b in zip(x,y))
        denominator = norm(x)*norm(y)
        return round(numerator/float(denominator),3)
    except ZeroDivisionError:
        return None

def euclidean(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def manhattan(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))

def minkowski(x,y,p_value):
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

def jaccard(x,y):
     intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
     union_cardinality = len(set.union(*[set(x), set(y)]))
     return intersection_cardinality/float(union_cardinality)
