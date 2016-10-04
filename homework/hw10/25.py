# Generators

def range_gen(start, end):
    """Returns a generator that iterates from start to end - 1.

    >>> for i in range_gen(0, 5):
    ...     print(i)
    ... 
    0
    1
    2
    3
    4
    """
    while start < end:
        yield start
        start += 1

def naturals():
    """Returns a generator that iterates over the natural numbers.

    >>> n = naturals()
    >>> next(n)  # Equivalent to n.__next__()
    0
    >>> next(n)
    1
    """
    curr = 0
    while True:
        yield curr
        curr += 1


# Iterating over binary search trees

class BST:
    empty = ()
    def __init__(self, entry, left=empty, right=empty):
        assert left is BST.empty or isinstance(left, BST)
        assert right is BST.empty or isinstance(right, BST)

        self.entry = entry
        self.left, self.right = left, right

        if left is not BST.empty: 
            assert left.max <= entry
        if right is not BST.empty: 
            assert entry < right.min
            
    @property
    def max(self): # Returns the maximum element in the tree
        if self.right is BST.empty:
            return self.entry
        return self.right.max

    @property
    def min(self): # Returns the minimum element in the tree
        if self.left is BST.empty:
            return self.entry
        return self.left.min

    def __iter__(self):
        """Iterates over the elements of the BST in order.
        An equivalent alternate implementation:

        for elem in self.left:
            yield elem
        yield self.entry
        for elem in self.right:
            yield elem
        """
        yield from self.left
        yield self.entry
        yield from self.right


# Coroutines

def match(pattern):
    """Receives and prints input that contains a pattern.

    >>> matcher = match('hello')
    >>> next(matcher)
    Looking for hello
    >>> matcher.send('hello there')
    hello there
    >>> matcher.send('goodbye now')
    >>> matcher.send('Othello is a great play')
    Othello is a great play
    >>> matcher.close()
    Done.
    """
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield)
            if pattern in s:
                print(s)
    except GeneratorExit:
        print('Done.')


# Sequence processing

def coroutine(func):
    """Decorator that automatically preps coroutines for us."""
    def call_next_once(*args):
        cr = func(*args)
        next(cr)
        return cr
    return call_next_once

def producer(next_coroutines):
    """Accepts user input and sends it to next_coroutines."""
    try:
        while True:
            s = input('Send me data: ')
            for cr in next_coroutines:
                cr.send(s)
    except KeyboardInterrupt:
        for cr in next_coroutines:
            cr.close()

@coroutine
def filter(next_coroutines, pred, map):
    """Receives input and sends the result of calling map on the input to
    next_coroutines if the input satisfies pred.
    """
    try:
        while True:
            s = (yield)
            if pred(s):
                for cr in next_coroutines:
                    cr.send(map(s))
    except GeneratorExit:
        for cr in next_coroutines:
            cr.close()

@coroutine
def consumer():
    """Receives input and prints it."""
    print('Ready to print')
    try:
        while True:
            s = (yield)
            print(s)
    except GeneratorExit:
        print('Done.')


true = lambda s: True
identity = lambda s: s

printer = consumer()
matcher = filter([printer], lambda s: 'MARVIN' in s, identity)
matcher2 = filter([printer], lambda s: 'BRIAN' in s, identity)
caps = filter([matcher, matcher2], true, lambda s: s.upper())

# To start the pipeline:
# producer([caps])


# THE CALCULATOR EXAMPLE BEGINS HERE
# The relevant changes occur at the bottom, to the REPL

from functools import reduce
from operator import add, sub, mul, truediv


# Constants

SYMBOLS = {'(', ')', '+', '-', '*', '/'}

def calc_add(*args):
    return reduce(add, args, 0)

def calc_sub(*args):
    if len(args) == 0:
        raise TypeError('not enough arguments to -')
    if len(args) == 1:
        return -args[0]
    return reduce(sub, args[1:], args[0])

def calc_mul(*args):
    return reduce(mul, args, 1)

def calc_div(*args):
    if len(args) == 0:
        raise TypeError('not enough arguments to /')
    if len(args) == 1:
        return 1 / args[0]
    return reduce(truediv, args[1:], args[0])

OPERATORS = {'+': calc_add, '-': calc_sub,
             '*': calc_mul, '/': calc_div}


# The Pair class

class Pair:
    """Represents the built-in pair data structure in Scheme."""
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return 'Pair({}, {})'.format(repr(self.first), repr(self.second))

    def __str__(self):
        result = '(' + str(self.first)
        while isinstance(self.second, Pair):
            self = self.second
            result += ' ' + str(self.first)
        if self.second is nil:
            return result + ')'
        return result + ' . ' + str(self.second) + ')'

    def __len__(self):
        return 1 + len(self.second)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.second[i-1]

    def map(self, fn):
        return Pair(fn(self.first), self.second.map(fn))

class nil:
    """Represents the special empty pair nil in Scheme."""
    def __repr__(self):
        return 'nil'

    def __str__(self):
        return '()'

    def __len__(self):
        return 0

    def __getitem__(self, i):
        raise IndexError('Index out of range')

    def map(self, fn):
        return nil

nil = nil()


# Parsing: Lexical Analysis

def tokenize(string):
    """Splits the provided string into a list of tokens."""
    string = string.replace('(', ' ( ')
    string = string.replace(')', ' ) ')
    tokens = string.split()
    if tokens.count('(') != tokens.count(')'):
        raise SyntaxError('unbalanced parentheses')
    for i in range(len(tokens)):
        token = tokens[i]
        if token not in SYMBOLS:
            to_num = numberize(token)
            if to_num == None:
                raise SyntaxError('unexpected token: ' + str(token))
            tokens[i] = to_num
    return tokens

def numberize(exp):
    """Converts exp to a number if possible, otherwise returns None."""
    try:
        return int(exp)
    except ValueError:
        try:
            return float(exp)
        except ValueError:
            return None


# Parsing: Syntactic Analysis

def read_exp(tokens):
    """Given a list of tokens, returns the first calculator expression
    (either a number, operator, or Pair).
    """
    token = tokens.pop(0)
    if token == '(':  # Start of a Pair
        exp = read_tail(tokens)
        if exp is nil:
            raise TypeError('nil is not a valid expression')
        return exp
    elif token == ')':  # End of a Pair?
        raise SyntaxError('unexpected )')
    else:  # operator or number
        return token

def read_tail(tokens):
    """Reads up to and including the matching close parenthesis,
    then forms a combination out all of the values read up to that point.
    """
    if tokens[0] == ')':  # Finished
        tokens.pop(0)
        return nil
    return Pair(read_exp(tokens), read_tail(tokens))


# Evaluation

def calc_eval(exp):
    """Evaluates a Calculator expression."""
    if isinstance(exp, Pair):
        op = calc_eval(exp.first)
        args = list(exp.second.map(calc_eval))
        return calc_apply(op, args)
    elif exp in OPERATORS:
        return OPERATORS[exp]
    else:  # Just a number
        return exp

def calc_apply(op, args):
    """Applies an operator to a Pair of arguments."""
    return op(*args)


# Read-Eval-Print Loop

def coroutine(func):
    """Decorator that automatically preps coroutines for us."""
    def call_next_once(*args):
        cr = func(*args)
        next(cr)
        return cr
    return call_next_once

@coroutine
def filter(fn, next_coroutine):
    try:
        while True:
            data = (yield)
            next_coroutine.send(fn(data))
    except GeneratorExit:
        next_coroutine.close()

@coroutine
def printer():
    try:
        while True:
            val = (yield)
            print(val)
    except GeneratorExit:
        print('\nCalculation completed.')

def event_loop(callback):
    try:
        while True:
            line = input('calc> ')
            while line.count('(') > line.count(')'):
                line += ' ' + input('      ')
            callback.send(line)
    except KeyboardInterrupt:
        callback.close()


# Create the REPL pipeline

display = printer()
eval = filter(calc_eval, display)
parse = filter(read_exp, eval)
lex = filter(tokenize, parse)

# To start the interpreter:
# event_loop(lex)

