import math

from rpn.operators.rpn_operator import Operator


def ip(value):
    return math.modf(value)[1]

def fp(value):
    return math.modf(value)[0]

family_name = 'Mathematical Functions'
family = [
    Operator('round', 'Round', 1, round),
    Operator('ceil', 'Ceiling', 1, math.ceil),
    Operator('floor', 'Floor', 1, math.floor),
    Operator('abs', 'Absolute Value', 1, math.fabs),
    Operator('ip', 'Integer Part', 1, ip),
    Operator('fp', 'Fractional Part', 1, fp),
    Operator('sqrt', 'Square Root', 1, math.sqrt),
    Operator('pow', 'Raise to a Power', 2, math.pow),
    Operator('exp', 'Exponentiation', 1, math.exp),
    Operator('log', 'Logarithm', 2, math.log),
    Operator('ln', 'Natural Logarithm', 1, math.log),
    Operator('fact', 'Factorial', 1, math.factorial),
]
