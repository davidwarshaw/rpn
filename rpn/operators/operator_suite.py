from rpn.operators import arithmetic
from rpn.operators import boolean
from rpn.operators import bitwise
from rpn.operators import mathematical_functions
from rpn.operators import trigonometric
from rpn.operators import stack
from rpn.operators import constants
from rpn.operators import options

macro_keyword = 'macro'
repeat_keyword = 'repeat'
exit_keyword = 'exit'

booleans = {'true': 1, 'false': 0}

families = {
    arithmetic.family_name: arithmetic.family,
    boolean.family_name: boolean.family,
    bitwise.family_name: bitwise.family,
    mathematical_functions.family_name: mathematical_functions.family,
    trigonometric.family_name: trigonometric.family,
    constants.family_name: constants.family,
    stack.family_name: stack.family,
    options.family_name: options.family,
}
lookup = {}
for family_name, family in families.items():
    for operator in family:
        lookup[operator.symbol] = operator

def symbols():
    return lookup.keys()

def reserved():
    return list(lookup.keys()) + list(booleans.keys()) + [macro_keyword, repeat_keyword, exit_keyword]

def print_table():
    for family_name, family in families.items():
        print(f'\n{family_name}\n')
        for operator in family:
            print(f'  {operator.symbol}\t{operator.name} ({operator.arity})')
