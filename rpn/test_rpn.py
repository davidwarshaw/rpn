import math
import rpn

entrands_test_cases = [
    [['1', '2', '+'], 3.0],
    [['1', '2', '+', '2', '-'], 1.0],
    [['-1', '2', '*', '-1', '*'], 2.0],
    [['1', '2', '+', '2', '/'], 1.5],
    [['2', '3', '/'], 0.6666666666666666],
    [['0', '3', '/'], 0],
    [['2', '3', '//'], 0],
    [['3', '2', '//'], 1],
    [['3', '2', '%'], 1],
    [['1', '++'], 2],
    [['2', '--'], 1],
    # Boolean
    [['1', '!', '!'], True],
    [['1', '1', '&&'], True],
    [['1', '0', '&&'], False],
    [['0', '0', '&&'], False],
    [['1', '1', '||'], True],
    [['1', '0', '||'], True],
    [['0', '0', '||'], False],
    [['1', '1', '^^'], False],
    [['1', '0', '^^'], True],
    [['0', '0', '^^'], False],
    # Bitwise
    [['0b0011', '~'], -4],
    [['0b0011', '0b1100', '|'], 0b1111],
    [['0b1111', '0b1000', '&'], 0b1000],
    [['0b1111', '0b1000', '^'], 0b0111],
    # Comparison
    [['1', '2', '<'], True],
    [['2', '2', '<'], False],
    [['1', '2', '<='], True],
    [['2', '2', '<='], True],
    [['2', '1', '=='], False],
    [['2', '2', '=='], True],
    [['2', '1', '!='], True],
    [['2', '2', '!='], False],
    [['2', '1', '>'], True],
    [['2', '2', '>'], False],
    [['2', '1', '>='], True],
    [['2', '2', '>='], True],
    # Trig
    [['0', 'sin'], 0],
    [['0', 'cos'], 1],
    [['0', 'tan'], 0],
    [['0', 'asin'], 0],
    [['1', 'acos'], 0],
    [['0', 'atan'], 0],
    [['0', 'sinh'], 0],
    [['1', 'cosh'], 1.5430806348152437],
    [['0', 'tanh'], 0],
    # Functions
    [['1.5', 'round'], 2],
    [['1.5', 'ceil'], 2],
    [['1.5', 'floor'], 1],
    [['-1', 'abs'], 1],
    [['1.5', 'ip'], 1],
    [['1.5', 'fp'], 0.5],
    [['4', 'sqrt'], 2],
    [['2', '3', 'pow'], 8],
    [['0', 'exp'], 1],
    [['100', '10', 'log'], 2],
    [['1', 'ln'], 0],
    [['50', 'fact'], 30414093201713378043612608166064768844377641568960512000000000000],
    # Stack
    [['cla'], ' '],
    [['1', '2', '1', '1', 'pick', '<'], True],
    [['cla'], ' '],
    [['1', '2', '1', 'drop', '<'], True],
    [['cla'], ' '],
    [['1', '2', '1', '1', '2', 'dropn', '<'], True],
    [['cla'], ' '],
    [['1', 'dup', '+'], 2],
    [['cla'], ' '],
    [['1', '4', 'dupn', '+', '+', '+'], 4],
    [['cla'], ' '],
    [['1', '2', '3', '2', 'roll', '+'], 4],
    [['cla'], ' '],
    [['1', '2', '3', '2', 'rolld', '+'], 3],
    [['cla'], ' '],
    [['1', '2', 'swap', '>'], True],
    [['cla'], ' '],
    # Constants
    [['pi', 'cos'], -1],
    [['e', 'ln'], 1],
    [['tau', '2', '*', 'cos'], 1],
    [['inf', '1', '+'], math.inf],
    [['nan', 'nan', '=='], False],

    # Variables
    [['1', 'a=', '2', 'b=', 'a', 'b', '+'], 3],
    [['1', 'a=', '2', 'B=', '2', 'a=', 'a', 'b', '+'], 4],
    # Macros
    [['cla'], ' '],
    [['macro', 'KIB', '1024', '*'], ' '],
    [['3', 'kib'], 3072],
    [['macro', 'mb', '1', 'kib', '10', '*'], 3072],
    [['1', 'mb'], 10240],
]

print('\n\n')
for inputs, expected in entrands_test_cases:
    rpn.consume_entrands(inputs)
    actual = rpn.peek()
    result = actual == expected
    print()
    print(f'inputs: {inputs}')
    print(f'{result} actual: {actual} expected: {expected}')
    assert(result)

encapsulated_test_cases = [
    ['\'1 2 + 3 * 10\'', ['1', '2', '+', '3', '*', '10']],
    ['\'   1 2 + 3 * 10   \t\'', ['1', '2', '+', '3', '*', '10']]
]

print('\n\n')
for inputs, expected in encapsulated_test_cases:
    actual = rpn.unencapsulate(inputs)
    result = actual == expected
    print()
    print(f'inputs: {inputs}')
    print(f'{result} actual: {actual} expected: {expected}')
    assert(result)

rpn.operator_suite.print_table()

print(f'\nTest cases: {len(entrands_test_cases) + len(encapsulated_test_cases)}\n')
