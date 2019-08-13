def key_from_comp(comp) :
    """ 
    Returns a callable class that takes one argument and
    creates a comparable instance that uses comp.
    Similar to functools.cmp_to_key

    Parameters
    ----------
    comp : function, required
        comp must be a function that takes two inputs such that
            comp(a,b) < 0  if a is considerd smaller than b
            comp(a,b) == 0 if a is considered equal to  b
            comp(a,b) > 0  if a is considered greater that b
    """
    class ComparisonClass :
        def __init__(self, val) :
            self.val = val 
        def __lt__(self, other) :
            return comp(self.val, other.val) < 0 
        def __eq__(self, other) :
            return comp(self.val, other.val) == 0
        def __gt__(self, other) :
            return comp(self.val, other.val) > 0 
    return ComparisonClass
