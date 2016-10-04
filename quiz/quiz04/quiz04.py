# Linked List abstraction

empty = 'X'

def link(first, rest=empty):
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(lnk):
    assert is_link(lnk), 'first only applies to linked lists.'
    assert lnk != empty, 'empty linked list has no first element.'
    return lnk[0]

def rest(lnk):
    assert is_link(lnk), 'rest only applies to linked lists.'
    assert lnk != empty, 'empty linked list has no rest.'
    return lnk[1]

def is_link(lnk):
    return lnk == empty or \
        type(lnk) == list and len(lnk) == 2 and is_link(lnk[1])

# Useful print_link function, used for testing.

def print_link(lnk):
    """Prints out a non-deep linked list."""
    line = ''
    while lnk != empty:
        if line:
            line += ' '
        line += str(first(lnk))
        lnk = rest(lnk)
    print('<{}>'.format(line))

def deep_reverse(lnk):
    """Return a reversed version of a possibly deep linked list lnk.

    >>> print_link(deep_reverse(empty))
    <>
    >>> print_link(deep_reverse(link(1, link(2, empty))))
    <2 1>

    >>> deep = link(1, link(link(2, link(3, empty)), empty))
    >>> deep_reversed = deep_reverse(deep)
    >>> print_link(first(deep_reversed))
    <3 2>
    >>> first(rest(deep_reversed))
    1
    >>> rest(rest(deep_reversed)) == empty
    True
    

    """
    "*** YOUR CODE HERE ***"
    def reverse(linked_list):
        if linked_list == empty:
            return empty
        f, r = first(linked_list), rest(linked_list)
        if not is_link(f):
            if r != empty:
                return link(reverse(r), link(f, reverse(rest(r))))
            else:
                return f
        return reverse(f)
    return reverse(lnk) 

# Tree abstraction

def tree(entry, children=[]):
    return [entry] + list(children)

def entry(tree):
    return tree[0]

def children(tree):
    return tree[1:]

def is_leaf(tree):
    return not children(tree)

# Useful print_tree function, used for testing

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(entry(t)))
    for child in children(t):
        print_tree(child, indent + 1)

def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hellooo')
    False
    >>> has_path(greetings, 'heya')
    False

    """
    assert len(word) > 0, 'no path for empty words.'
    "*** YOUR CODE HERE ***"
    if len(word) == 1:
        return entry(t) == word
    head, rest = word[0], word[1:]
    if is_leaf(t):
        if len(word) == 1:
            return entry(t) == head
        else:
            # index out of range
            return False
    elif entry(t) == head:
        return True in [has_path(tr, rest) for tr in children(t)]
    else:
        return False
