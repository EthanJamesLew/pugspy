"""
PUGS set similarity modules

Ethan Lew
11/10/15
"""
from math import*
from decimal import Decimal

def norm(x):
    return round(sqrt(sum([a*a for a in x])),3)

def nth_root(value, n_root):
    try:
        root_value = 1/float(n_root)
        return round (Decimal(value) ** Decimal(root_value),3)
    except ZeroDivisionError:
        return None

def cosine(x,y):
    try:
        numerator = sum(a*b for a,b in zip(x,y))
        denominator = norm(x)*norm(y)
        return round(numerator/float(denominator),3)
    except ZeroDivisionError:
        return None

def euclidean(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def manhattan_distance(x,y):
    return sum(abs(a-b) for a,b in zip(x,y))

def minkowski_distance(x,y,p_value):
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

def jaccard_similarity(x,y):
     intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
     union_cardinality = len(set.union(*[set(x), set(y)]))
     return intersection_cardinality/float(union_cardinality)
