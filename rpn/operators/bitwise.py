import operator

from rpn.operators.rpn_operator import Operator


family_name = 'Bitwise'
family = [
    Operator('~', 'Bitwise NOT', 1, operator.invert),
    Operator('&', 'Bitwise AND', 2, operator.and_),
    Operator('|', 'Bitwise OR', 2, operator.or_),
    Operator('^', 'Bitwise XOR', 2, operator.xor),
    Operator('<<', 'Left Shift', 2, operator.lshift),
    Operator('>>', 'Right Shift', 2, operator.rshift),
]
