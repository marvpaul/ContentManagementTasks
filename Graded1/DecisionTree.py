import math
def computeEntropy(probs):
    propability = 0
    for p in probs:
        if p != 0:
            propability -= p * math.log2(p)
    return propability

def computeProps(data):
    props = []
    size = len(data)
    amount_class1 = 0
    amount_class2 = 0
    for entry in data:
        if int(entry['Survived']) == 0:
            amount_class1 += 1
        else:
            amount_class2 += 1
    props.append(amount_class1 / size)
    props.append(amount_class2 / size)
    return props