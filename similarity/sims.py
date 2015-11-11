"""
This file contains set similarity modules
"""
from math import*

def norm(x):

   return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
 numerator = sum(a*b for a,b in zip(x,y))
 denominator = norm(x)*norm(y)
 return round(numerator/float(denominator),3)
