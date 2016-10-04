HW_SOURCE_FILE = 'hw03.py'


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    l = [1, 2, 3]
    for i in range(4, n + 1):
        l += [l[i - 2] + 2 * l[i - 3] + 3 * l[i - 4]]
    return l[n - 1]


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    """ DESCRIPTION
    both asc and dec returns pingpong score the index of which is cnt
    """

    def swap(num):
        return has_seven(num) or num % 7 == 0

    def asc(k, cnt):
        """
        k: current score
        cnt: numbers counted
        """
        if n == cnt:
            return k
        elif swap(cnt):
            return dec(k - 1, cnt + 1)
        else:
            return asc(k + 1, cnt + 1)

    def dec(k, cnt):
        if n == cnt:
            return k
        elif swap(cnt):
            return asc(k + 1, cnt + 1)
        else:
            return dec(k - 1, cnt + 1)

    return asc(1, 1)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.
    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    from math import log, floor, pow

    def helper(n, m):
        """
            n: number of cents
            m: maximum partition of cents (2^m)
        """
        if n == 1 or n == 0 or m == 0:
            return 1
        elif n < 0:
            return 0
        else:
            return helper(n - pow(2, m), m) + helper(n, m - 1)

    return helper(amount, floor(log(amount, 2)))


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    # check if variables are correct
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if start == 1:
        if end ==2:
            temp = 3
        else:
            temp = 2
    elif start == 2:
        if end == 1:
            temp = 3
        else:
            temp = 1
    else:
        if end == 1:
            temp = 2
        else:
            temp = 1

    def helper(n, start, end, temp):
        if n == 0:
            return 1
        helper(n - 1, start, temp, end)
        print_move(start, end)
        helper(n - 1, temp, end, start)

    helper(n, start, end, temp)


def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    return sum(([k] if type(k)==int else flatten(k) for k in lst), [])


def merge(list1, list2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    if len(list1) == 0 and len(list2) > 0:
        return list2
    elif len(list2) == 0 and len(list1) > 0:
        return list1
    elif len(list1) == 0:
        return []
    elif list1[0] <= list2[0]:
        temp = [list1[0]]
        return temp + merge(list1[1:], list2)
    else:
        temp = [list2[0]]
        return temp + merge(list1, list2[1:])

def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    "*** YOUR CODE HERE ***"

    length = len(seq)
    # Base Case
    if length <= 1:
        return seq
    else:
        mid = length // 2
        left = mergesort(seq[:mid])
        right = mergesort(seq[mid:])
        return merge(left, right)


###################
# Extra Questions #
###################

from operator import sub, mul


def Y(f):
    """The Y ("paradoxical") combinator."""
    return f(lambda: Y(f))


def Y_tester():
    """
    >>> tmp = Y_tester()
    >>> tmp(1)
    1
    >>> tmp(5)
    120
    >>> tmp(2)
    2
    """
    "*** YOUR CODE HERE ***"
    return Y(________)  # Replace
