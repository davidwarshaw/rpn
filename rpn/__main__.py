#!/usr/bin/env python

import os
import sys
import re
from pathlib import Path
from ast import literal_eval
from collections import deque
from inspect import signature

from rpn.operators import operator_suite


stack = deque()
vars = {}
options = {
    'stack_display_horizontal': True,
    'output_format': 'n'
}
default_padding = {'n': '0', 'b': '8', 'x': '2', 'o': '4'}

PROMPT_COLOR = '\033[34m'
STACK_COLOR = '\033[96m'
ERROR_COLOR = '\033[91m'
STOP_COLOR = '\033[0m'

def format_error(i, entrand, message):
    return f'Error at entrand: {entrand}: {message}'

def format_integer(integer):
    code = options['output_format']
    format_string = '{:0' + default_padding[code] + code + '}'
    return format_string.format(integer)

def format_prompt():
    return PROMPT_COLOR + ' > ' + STOP_COLOR

def format_stack():
    formatted_items = []
    for item in stack:
        if isinstance(item, int):
            formatted_items.append(STACK_COLOR + format_integer(item) + STOP_COLOR)
        else:
            formatted_items.append(STACK_COLOR + str(item) + STOP_COLOR)

    if options['stack_display_horizontal']:
        return ' '.join(formatted_items)

    formatted_items.reverse()
    return '\n'.join(formatted_items) + '\n'

def peek():
    return stack[-1] if len(stack) > 0 else ' '

def consume_entrands(entrands):
    try:
        entrands = deque([entrand.lower() for entrand in entrands if len(entrand) > 0])
        while entrands:
            try:
                entrand = entrands.popleft()
            except IndexError:
                raise RpnError(entrand, f'no operands on stack')

            # Operators
            if entrand in operator_suite.symbols():
                operator = operator_suite.lookup[entrand]

                # Inspect the application signature to add the stack and vars if they are specified as
                # function parameters.
                #
                # NOTE: Inspecting signature will fail on some implementations linked to c libs.
                #       If it fails, then the function cannot need the stack and vars.
                #
                try:
                    params = list(signature(operator.apply).parameters.keys())
                except ValueError:
                    params = []
                needs_stack = set(['stack', 'vars']).issubset(set(params))

                try:
                    if operator.arity == 0:
                        result = operator.apply(stack, vars, options) if needs_stack else operator.apply()
                        if result is not None:
                            stack.append(result)
                    elif operator.arity == 1:
                        operand = stack.pop()
                        result = operator.apply(operand, stack, vars, options) if needs_stack else operator.apply(operand)
                        if result is not None:
                            stack.append(result)
                    elif operator.arity == 2:
                        operand_2 = stack.pop()
                        operand_1 = stack.pop()
                        result = operator.apply(operand_1, operand_2)
                        if result is not None:
                            stack.append(result)
                    else:
                        raise RpnError(entrand, f'operator with arity {operator.arity}: arity must be in [0, 2]')

                except IndexError:
                    raise RpnError(entrand, f'too few operands on stack')
                except ZeroDivisionError:
                    raise RpnError(entrand, f'division by zero')

            # Boolean values
            elif entrand in operator_suite.booleans.keys():
                stack.append(operator_suite.booleans[entrand])

            # Variable and Macro evaluation
            elif entrand in vars.keys():
                var = vars[entrand]
                if isinstance(var, deque):
                    # The var deque must be reversed before being pushed onto the left of the
                    # existing entrands, because it be consumed from its left
                    var.reverse()
                    entrands.extendleft(var)
                else:
                    stack.append(var)

            # Variable assignment
            elif entrand and entrand[-1] == '=':
                varname = entrand[:-1]
                if varname in operator_suite.reserved():
                    raise RpnError(entrand, f'cannot assign to variable {varname}: reserved word')
                if not varname.isidentifier():
                    raise RpnError(entrand, f'cannot assign to variable {varname}: not a valid identifier')

                vars[varname] = stack.pop()

            # Macro definition
            elif entrand == operator_suite.macro_keyword:
                varname = entrands.popleft()
                if varname in operator_suite.reserved():
                    raise RpnError(entrand, f'cannot assign to macro {varname}: reserved word')
                if not varname.isidentifier():
                    raise RpnError(entrand, f'cannot assign to variable {varname}: not a valid identifier')

                # Defining a macro consumes all remaining entrands
                vars[varname] = deque(entrands)
                entrands.clear()

            # Macro definition
            elif entrand == operator_suite.repeat_keyword:
                try:
                    operand = stack.pop()
                    operators = deque(entrands) * round(operand)
                    # Repeat consumes all remaining entrands
                    entrands.clear()
                    operators.reverse()
                    entrands.extendleft(operators)
                except IndexError:
                    raise RpnError(entrand, f'too few operands on stack')

            # Exit the shell
            elif entrand == operator_suite.exit_keyword:
                sys.exit(0)

            # Numbers
            else:
                try:
                    number = literal_eval(entrand)
                    stack.append(number)
                except Exception:
                    raise RpnError(entrand, f'unrecognized as operator, boolean, var, macro, repeat, or numeric input')

    except RpnError as e:
        print(e)

def unencapsulate(cl):
    encapsulators = ['\'', '"']
    if cl[0] in encapsulators and cl[-1] in encapsulators:
        return re.sub(r'\s+', ' ', cl[1:-1]).strip().split(' ')
    return cl

def tokenize_line(line):
    return re.sub(r'\s+', ' ', line).strip().split(' ')

def print_help():
    print('\nUSAGE\n')
    print('  rpn                            Launch in interactive mode. Exit with ctrl-d or \'exit\'')
    print('  rpn [expression]               Evaluate expression from command line, outputting top stack operand')
    print('  cat expressions.list | rpn     Evaluate expression from each line of stdin, outputting top stack operand')
    print('  rpn --help                     Print this screen')
    print()
    print('\nRC FILE\n')
    print('  rpn will execute the contents of ~/.rpnrc at startup if it exists.')
    print('\nEXAMPLES\n')
    print('  > 1 2 + 3 + 4 + 5 +            => 15')
    print('  > pi cos                       => -1.0')
    print('\nVARIABLES\n')
    print('  > 1 a= 2 b= a b *              => 2')
    print('\nMACROS\n')
    print('  > macro kib 1024 *             => (no output)')
    print('  > macro 3 kib                  => 3072')
    print('\nREPETITION\n')
    print('  > 1 2 3 4 3 repeat +           => 10')
    print('\nFORMATS\n')
    print('  > 255 bin                      => 11111111')
    print('  > 0b11111111 dec               => 255')
    print('  > 255 hex                      => ff')
    print('  > 0xff hex                     => 255')
    print('  > 255 oct                      => 0377')
    print('  > 0o0377 dec                   => 255')
    print('\nOPERATORS\n')
    print('  symbol name (number of operands consumed from stack)')
    operator_suite.print_table()
    print()

class RpnError(Exception):

    def __init__(self, entrand, message):
        self.preamble = f'Error at entrand: {entrand}: '
        self.message = message

    def __str__(self):
        return ERROR_COLOR + self.preamble + self.message + STOP_COLOR

if __name__ == '__main__':
    cl_tokens = sys.argv[1:]
    num_cl_tokens = len(cl_tokens)

    # Check early for the help screen
    if '--help' in ' '.join(cl_tokens).lower():
        print_help()
        sys.exit(0)

    # Read the rc file (if it exists)
    rc_file = Path(os.path.expanduser('~/.rpnrc'))
    if rc_file.is_file():
        with open(rc_file, 'r') as file:
            for line in file:
                line_tokens = tokenize_line(line.lower())
                consume_entrands(line_tokens)

    # Interactive mode or file mode
    if num_cl_tokens == 0:

        # Interactive mode
        if sys.stdin.isatty():
            while True:
                try:
                    line = input(format_stack() + format_prompt())
                    line_tokens = tokenize_line(line.lower())
                    consume_entrands(line_tokens)
                except EOFError:
                    print()
                    break

        # File/Pipe mode
        else:
            for line in sys.stdin:
                line_tokens = tokenize_line(line.lower())
                consume_entrands(line_tokens)
                print(peek())

    # Take from command line, encapsulated
    elif num_cl_tokens == 1:
        unencapsulated_cl_tokens = unencapsulate(cl_tokens)
        consume_entrands(unencapsulated_cl_tokens)
        print(peek())
    # Take from command line, unencapsulated
    else:
        consume_entrands(cl_tokens)
        print(peek())
