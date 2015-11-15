from math import sqrt
def mean(lst):
    """calculates mean"""
    return sum(lst) / len(lst)

def stddev(lst):
    """returns the standard deviation of lst"""
    variance = 0
    mn = mean(lst)
    for e in lst:
        variance += (e-mn)**2
    variance /= len(lst)

    return sqrt(variance)
