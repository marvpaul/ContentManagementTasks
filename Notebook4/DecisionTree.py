import math


def computeEntropy(probs):
    propability = 0
    for p in probs:
        propability -= p * math.log2(p)
    return propability


print(computeEntropy([1/3, 2/3]))