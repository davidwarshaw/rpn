import math

from rpn.operators.rpn_operator import Operator


family_name = 'Constants'
family = [
    Operator('pi', 'π = 3.141592…', 0, lambda: math.pi),
    Operator('tau', 'τ = 6.283185…', 0, lambda: math.tau),
    Operator('e', 'e = 2.718281…', 0, lambda: math.e),
    Operator('inf', 'Floating Point Positive Infinity', 0, lambda: math.inf),
    Operator('nan', 'Floating Point \"Not a Number\" value', 0, lambda: math.nan),
]
