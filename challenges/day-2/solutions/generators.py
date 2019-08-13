import random

def shuffle_gen(start, stop) :
    """ A generator that yields a random permutation
    of the numbers start, start + 1, ..., stop -1. """
    n = stop - start
    scratch = dict()
    for remaining in range(n, 0, -1):
        i = random.randrange(remaining)
        # recall that scratch.get(i,i) = scratch[i]
        # if it is defined and scratch.get(i,i) = i otherwise
        yield scratch.get(i,i) + start
        scratch[i] = scratch.get(remaining - 1, remaining - 1)
        # we don't need to keep track of this anymore
        # note : we use `.pop` instead of `del` because
        # scratch[remaining - 1] may not be set
        scratch.pop(remaining - 1, None)
