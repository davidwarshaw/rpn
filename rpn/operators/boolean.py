import operator

from rpn.operators.rpn_operator import Operator


def and_(value1, value2):
    return value1 and value2

def or_(value1, value2):
    return value1 or value2

family_name = 'Boolean'
family = [
    Operator('!', 'Boolean NOT', 1, operator.not_),
    Operator('&&', 'Boolean AND', 2, operator.and_),
    Operator('||', 'Boolean OR', 2, operator.or_),
    Operator('^^', 'Boolean XOR', 2, operator.ne),
    Operator('<', 'Less Than', 2, operator.lt),
    Operator('<=', 'Less Than or Equal to', 2, operator.le),
    Operator('==', 'Equal to', 2, operator.eq),
    Operator('!=', 'Not Equal to', 2, operator.ne),
    Operator('>', 'Greater Than', 2, operator.gt),
    Operator('>=', 'Greater Than or Equal to', 2, operator.ge),
]
