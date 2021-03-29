import math

from rpn.operators.rpn_operator import Operator

family_name = 'Trigonometric'
family = [
    Operator('sin', 'Sine', 1, math.sin),
    Operator('cos', 'Cosine', 1, math.cos),
    Operator('tan', 'Tangent', 1, math.tan),
    Operator('asin', 'Arc Sine', 1, math.asin),
    Operator('acos', 'Arc Cosine', 1, math.acos),
    Operator('atan', 'Arc Tangent', 1, math.atan),
    Operator('sinh', 'Hyperbolic Sine', 1, math.sinh),
    Operator('cosh', 'Hyperbolic Cosine', 1, math.cosh),
    Operator('tanh', 'Hyperbolic Tangent', 1, math.tanh),
]
