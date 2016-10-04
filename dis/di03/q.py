def sum_range(lower, upper):
    """
    >>> sum_range(45, 60)
    True
    >>> sum_range(40, 55)
    False
    >>> sum_range(170, 201)
    True
    """
    assert lower <= upper, 'invalid imput'
    def helper(pmin, pmax):
        # Base Case
        if pmin <= lower and lower < pmax:
            return True
        elif pmax <= lower:
            return False
        return helper(pmin + 50, pmax + 60) or helper(pmin + 130, pmax + 140)

    return helper(0, 0)
