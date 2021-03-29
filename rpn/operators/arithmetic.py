import operator

from rpn.operators.rpn_operator import Operator


def inc(value):
    return value + 1

def dec(value):
    return value - 1

family_name = 'Arithmetic'
family = [
    Operator('+', 'Addition', 2, operator.add),
    Operator('-', 'Subtraction', 2, operator.sub),
    Operator('*', 'Multiplication', 2, operator.mul),
    Operator('/', 'Division', 2, operator.truediv),
    Operator('//', 'Floor Division', 2, operator.floordiv),
    Operator('%', 'Modulo', 2, operator.mod),
    Operator('++', 'Increment', 1, inc),
    Operator('--', 'Decrement', 1, dec),
]
