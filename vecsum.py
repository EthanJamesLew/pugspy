"""
First attempt implementation of a monte carlo based method of getting users to sum to a project
"""

import similarity
from itertools import islice, combinations_with_replacement
from functools import reduce
from math import factorial
from operator import mul
import random
import time

def _enumVec(total, length):
    # get all possible ways of choosing 10 of our indices
    # for example, the first one might be  0000000000
    # meaning we picked index 0 ten times, for [10, 0, 0]
    for t in combinations_with_replacement(range(length), total+1):
        cand = [0] * length
        for i in t:
            cand[i] += 1
        yield list(cand)

def vectorSum(total, length):
    num_outcomes = reduce(mul, range(total + 1, total + length)) // factorial(length - 1)
    # that's integer division, even though SO thinks it's a comment :)
    idx = random.choice(range(num_outcomes))
    try:
        t = next(islice(_enumVec(total, length), idx, None))
        return t
    except StopIteration:
        t = next(islice(_enumVec(total, length), idx, None))
        time.sleep(5)
        return t

def getDecomp(bases, vec):
    ansMatrix=[]
    for i in range(0, len(bases[0])):
        vector=vectorSum(vec[i], len(bases))
        ansMatrix.append(vector)
    transpose = map(list, zip(*ansMatrix))
    return transpose

def basesdecomp(bases, vec):
    best = float('inf')
    bestans = []
    cosineval = float('inf')
    for i in range(0, 1000):
        ans = getDecomp(bases, vec)
        try:
            cosineval = similarity.stddev([similarity.cosine(x, y) for x,y in zip(ans,bases)])
        except TypeError:
            None
        if cosineval < best:
            best = cosineval
            project = [similarity.cosine(x, y) for x,y in zip(ans,bases)]
            bestans = ans
    for i in range(1, len(ans)):
        sum1 = [x + y for x, y in zip(bases[i], bases[i-1])]
    fidelity = similarity.cosine(sum1, vec)
    return best, bestans, fidelity, project

if __name__=="__main__":
    users = [[9,9,1,3,12],[1,2,1,3,4],[2,3,4,2,4]]
    users = [similarity.unit(x) for x in users]
    constraints=[3.,2.,4.,4]
    project=[40,40,40,40,40]
    best = 0

    print basesdecomp(users, project)
