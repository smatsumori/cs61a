def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    lower = min(p1, p2, p3, p4)
    upper = max(p1, p2, p3, p4)
    return interval(lower, upper)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    p1 = lower_bound(x) - lower_bound(y)
    p2 = lower_bound(x) - upper_bound(y)
    p3 = upper_bound(x) - lower_bound(y)
    p4 = upper_bound(x) - upper_bound(y)
    lower = min(p1, p2, p3 ,p4)
    upper = max(p1, p2, p3 ,p4)
    return interval(lower, upper)

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert not (upper_bound(y) > 0 and lower_bound(y) < 0), 'Zero division error'
    assert upper_bound(y) != 0 or lower_bound(y) != 0, 'Zero dibision error'
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(1, 3) # Replace this line!
    r2 = interval(1, 3) # Replace this line!
    return r1, r2

def multiple_references_explanation():
    return "Alyssa is wrong, which means par1 is better than par2. The reason is because par1 uses less division function which makes rounded error when it handles irrational numbers."

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    def squere_interval(x):
        # Valuse set must be non-negative
        p1 = abs(lower_bound(x) * lower_bound(x))
        p2 = abs(lower_bound(x) * upper_bound(x))
        p3 = abs(upper_bound(x) * upper_bound(x))
        lower = min(p1, p2, p3)
        upper = max(p1, p2, p3)
        return interval(lower, upper)
    
    ex_point = -b/(2 * a)
    ex = a * (ex_point**2) + b * ex_point + c

    x1 = lower_bound(x)
    x2 = upper_bound(x)

    fx1 = a * (x1**2) + b * x1 + c
    fx2 = a * (x2**2) + b * x2 + c

    upper = max(fx1, fx2)
    lower = min(fx1, fx2)


    # if margin includes ex_point set ex
    if x1 < ex_point and ex_point < x2:
        if a > 0:
            lower = ex
        else:
            upper = ex
    return interval(lower, upper)


def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"

