# Generatorts

# Q1

def permutations(lst):
    """Generates all permutations of sequence LST.  Each permutation is a
    list of the elements in LST in a different order.

    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> type(permutations([1, 2, 3]))
    <class 'generator'>
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    # lazy evaluations
#    import pdb; pdb.set_trace()
    # convert a tuple to a list
    lst = list(lst)
    if not lst:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        # list = [1, 2, 3]
        # permutations returns set of permutated lists
        # todo Fix Type Error Tuple 
        for i in permutations(lst[1:]):
            for j in range(len(i) + 1):
                yield i[:j] + [lst[0]] + i[j:]

# Review

# Q2

def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power_of_two = 1.0
    "*** YOUR CODE HERE ***"
    # input = 13
    #   4 * 4 = 16
    i = 0.0
    if x < 1:
        while x < 1 / (2 ** i):
            i += 1
        return  1 / 2.0 ** i if (2**i - x) < (x - 2 ** (i - 1)) else 1 / 2.0 ** (i - 1)
    else:
        while 2 ** i < x:
            i += 1
        return 2.0**i if (i**2 - x) < (x - (i - 1) ** 2) else 2.0 ** (i - 1)

# Q3

def repeated(f, n):
    """Returns a single-argument function that takes a value, x, and applies
    the single-argument function F to x N times.
    >>> repeated(lambda x: x*x, 3)(2)
    256
    """
    def h(f_x):
        for k in range(n):
            f_x = f(f_x)
        return f_x
    # h is callable
    return h

def smooth(f, dx):
    """Returns the smoothed version of f, g where

    g(x) = (f(x - dx) + f(x) + f(x + dx)) / 3

    >>> square = lambda x: x ** 2
    >>> round(smooth(square, 1)(0), 3)
    0.667
    """
    "*** YOUR CODE HERE ***"
    return lambda x: ((f(x - dx) + f(x) + f(x + dx)) / 3)


def n_fold_smooth(f, dx, n):
    """Returns the n-fold smoothed version of f

    >>> square = lambda x: x ** 2
    >>> round(n_fold_smooth(square, 1, 3)(0), 3)
    2.0
    """
    "*** YOUR CODE HERE ***"
    # n_fold_smooth(square,
    # smooth is a lambda function
    # repeted returns a callable function
    # when smoothe gonna evaluate?
    # python evaluates left from right inside out
    # so it evaluates smooth(f, dx) first before it passes through repeted function
    # return repeated(smooth(f, dx), n)
    # applying smooth multipetimes doesn't change f multiple times
    # it only changes one time

    for i in range(n):
        f = smooth(f, dx)
    return f

# Q4

def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    "*** YOUR CODE HERE ***"
#     import pdb; pdb.set_trace()
    global_count = 0
    def make_counter():
        count = 0
        def cnt(message):
            nonlocal count
            nonlocal global_count
            s = message
            if s == 'count':
                count += 1
                print(count)
            elif s == 'reset':
                count = 0
            elif s == 'global-count':
                global_count += 1
                print(global_count)
            elif s == 'global-reset':
                global_count = 0
        return cnt

    return make_counter


# Q5

def deck(suits, ranks):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and ranks. Each element in the returned list should be of the form
    [suit, rank].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """
    "*** YOUR CODE HERE ***"
#    lst = []
#    for s in suits:
#        for r in ranks:
#            lst.append([s, r])
#    return lst

    return [[suit, rank] for suit in suits for rank in ranks]

# Q6

def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    "*** YOUR CODE HERE ***"
    # [1, 2, 3, 4, 5, 6]
    #  0  1  2  3  4  5
    #  0  1  0  1  0  1
    # [1, 2, 3] [4, 5, 6]
    # handle range
    # return [e1, e2 for e1 in deck[:len(deck)/2] for e2 in deck[len(deck)/2:]]
    from functools import reduce
    M = len(deck) // 2
    return list(reduce(lambda x, y: x + y, zip(deck[:M], deck[M:])))
    

# Q7

def is_circular(G):
    """Return true iff G represents a circular directed graph."""
    # check each vertex in G
    for v in G:
        if reaches_circularity(G, v):
            return True
    return False

def reaches_circularity(G, v0):
    """Returns true if there is a circularity in G in some path
    starting from vertex V0.
    >>> G = { 'A': ['B', 'D'], 'B': ['C'], 'C': ['F'], 'D': ['E'], 
    ...       'E': ['F'], 'F': ['G'], 'G': ['A'] }
    >>> is_circular(G)
    True
    >>> G['F'] = []
    >>> is_circular(G)
    False
    """
    "*** YOUR CODE HERE ***"
    visited = []
    def is_path_to_cycle(v1):
        nonlocal visited
        for w in G[v1]:
            if v0 == w:
                return True
            elif w in visited:
                # skip  if w is visited
                continue
            else:
                visited += [w]
                return is_path_to_cycle(w)
    return is_path_to_cycle(v0)



# Q8


class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

def intersection(xs, ys):
    """
    >>> a = Link(1)
    >>> intersection(a, Link.empty) is Link.empty
    True

    >>> b = a
    >>> intersection(a, b).first # intersection begins at a
    1

    >>> looks_like_a = Link(1)
    >>> intersection(a, looks_like_a) is Link.empty # no intersection! (identity vs value)
    True

    >>> b = Link(1, Link(2, Link(3, a)))
    >>> a.first = 5
    >>> intersection(a, b).first # intersection begins at a
    5

    >>> c = Link(3, b)
    >>> intersection(b, c).first # intersection begins at b
    1
    >>> intersection(c, b).first # intersection begins at b
    1

    >>> intersection(a, c).first # intersection begins at a
    5
    """
    "*** YOUR CODE HERE ***"
    def hlen(li):
        ptr = li
        cnt = 0
        while ptr is not Link.empty:
            ptr = ptr.rest
            cnt += 1
        return cnt

    length = hlen(ys) - hlen(xs)
    
    if length > 0:
        curr = ys
        while length > 0:
            curr = curr.rest
            length -= 1
        if curr is xs:
            return curr
        else:
            return Link.empty
    else:
        curr = xs
        while length < 0:
            curr = curr.rest
            length += 1
        if curr is ys:
            return curr
        else:
            return Link.empty

