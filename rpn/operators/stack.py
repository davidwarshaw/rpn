import math
from collections import deque

from rpn.operators.rpn_operator import Operator


def cla(stack, vars, options):
    stack.clear()
    vars.clear()

def clr(stack, vars, options):
    stack.clear()

def clv(stack, vars, options):
    vars.clear()

def pick(value, stack, vars, options):
    stack.rotate(value)
    operand = stack.pop()
    stack.rotate(-value)
    stack.append(operand)

def drop(stack, vars, options):
    dropn(1, stack, vars, options)

def dropn(value, stack, vars, options):
    for i in range(value):
        stack.pop()

def dup(stack, vars, options):
    dupn(1, stack, vars, options)

def dupn(value, stack, vars, options):
    for i in range(value):
        operand = stack.pop()
        stack.append(operand)
        stack.append(operand)

def roll(value, stack, vars, options):
    stack.rotate(value)

def rolld(value, stack, vars, options):
    stack.rotate(-value)

def swap(stack, vars, options):
    operand_2 = stack.pop()
    operand_1 = stack.pop()
    stack.append(operand_2)
    stack.append(operand_1)

family_name = 'Stack Operation'
family = [
    Operator('cla', 'Clear the stack, variables and macros', 0, cla),
    Operator('clr', 'Clear the stack', 0, clr),
    Operator('clv', 'Clear the variables and macros', 0, clv),
    Operator('pick', 'Pop the n-th operand from the stack', 1, pick),
    Operator('drop', 'Drop the top operand from the stack', 0, drop),
    Operator('dropn', 'Drop the top n operands from the stack', 1, dropn),
    Operator('dup', 'Duplicate the top operand on the stack', 0, dup),
    Operator('dupn', 'Duplicate the top n operands on the stack', 1, dupn),
    Operator('roll', 'Roll the stack upwards by n', 1, roll),
    Operator('rolld', 'Roll the stack downwards by n', 1, rolld),
    Operator('swap', 'Swap the top two stack operands', 0, swap),
]
