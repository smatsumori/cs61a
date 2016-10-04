# Linked Lists (do not modify the following class!)


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

# Q1

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    if link is Link.empty:
        return []
    return [link.first] + link_to_list(link.rest)

# Q2 (and Extra Question)

def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    if link.rest is Link.empty:
        return False

    else:
        curr = link.rest
        while curr is not Link.empty:
            if link == curr:
                return True
            curr = curr.rest
        return has_cycle(link.rest)

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"

# Trees (do not modify the following class!)

class Tree:
    def __init__(self, entry, children=[]):
        for c in children:
            assert isinstance(c, Tree)
        self.entry = entry
        self.children = children

    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.entry, children_str)

    def is_leaf(self):
        return not self.children

# Q3

def cumulative_sum(t):
    """Mutates t where each node's entry becomes the sum of all entries in the
    corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return t.entry
    else:
        for c in t.children:
            cumulative_sum(c)
        t.entry = t.entry + sum([c.entry for c in t.children])
    
# Q4

def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    """
    "*** YOUR CODE HERE ***"
    def bst_max(t):
        if t.is_leaf():
            return t.entry
        else:
            return max([t.entry] + [bst_max(c) for c in t.children])
    
    def bst_min(t):
        if t.is_leaf():
            return t.entry
        else:
            return min([t.entry] + [bst_min(c) for c in t.children])


    if t.is_leaf():
        return True

    elif len(t.children) == 2:
        return bst_max(t.children[0]) <= t.entry and t.entry < bst_min(t.children[1]) and all(is_bst(c) for c in t.children)
    
    elif len(t.children) == 1:
        return is_bst(t.children[0])
    
    else:
        return False


# Sets (do not modify the following function!)

import time

def timeit(func):
    """Returns the time required to execute FUNC() in seconds."""
    t0 = time.perf_counter()
    func()
    return time.perf_counter() - t0

# Q5

def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    >>> add_up(151, range(0, 200000, 2))
    False
    >>> timeit(lambda: add_up(151, range(0, 200000, 2))) < 1.0
    True
    >>> add_up(50002, range(0, 200000, 2))
    True
    """
    "*** YOUR CODE HERE ***"

# Q6

def missing_val(lst0, lst1):
    """Assuming that lst0 contains all the values in lst1, but lst1 is missing
    one value in lst0, return the missing value.  The values need not be
    numbers.

    >>> from random import shuffle
    >>> missing_val(range(10), [1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> big0 = [str(k) for k in range(15000)]
    >>> big1 = [str(k) for k in range(15000) if k != 293 ]
    >>> shuffle(big0)
    >>> shuffle(big1)
    >>> missing_val(big0, big1)
    '293'
    >>> timeit(lambda: missing_val(big0, big1)) < 1.0
    True
    """
    "*** YOUR CODE HERE ***"
