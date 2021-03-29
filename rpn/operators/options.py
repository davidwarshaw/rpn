import math
from collections import deque

from rpn.operators.rpn_operator import Operator


def stack(stack, vars, options):
    options['stack_display_horizontal'] = not options['stack_display_horizontal']

def names(stack, vars, options):
    print()
    for var, value in vars.items():
        if not isinstance(value, deque):
            print(f'  {var}= {value}')
    print()
    for var, value in vars.items():
        if isinstance(value, deque):
            print(f'  {var} [{", ".join(value)}]')
    print()

def dec(stack, vars, options):
    options['output_format'] = 'n'

def bin(stack, vars, options):
    options['output_format'] = 'b'

def hex(stack, vars, options):
    options['output_format'] = 'x'

def oct(stack, vars, options):
    options['output_format'] = 'o'

family_name = 'System'
family = [
    Operator('names', 'Print current variables and macros', 0, names),
    Operator('stack', 'Toggle stack display between horizontal and vertical', 0, stack),
    Operator('dec', 'Output stack integers as decimal', 0, dec),
    Operator('bin', 'Output stack integers as binary', 0, bin),
    Operator('hex', 'Output stack integers as hex', 0, hex),
    Operator('oct', 'Output stack integers as octal', 0, oct),
]
