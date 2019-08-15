import numpy as np

def evolution(seed) :
    # cuts down on the verbosity
    nbrs_count = sum(np.roll(seed, (i,j), (0,1))
                     for i in (-1, 0, 1) for j in (-1, 0, 1)
                     if (i != 0 or j != 0))
    
    y = (nbrs_count == 3) | (seed & (nbrs_count == 2))
    y[(0,-1),:] = False
    y[:,(0,-1)] = False
    return y

# verbose, but with out any loops at all
def neighbor_count(seed) :
    down = np.roll(seed,1,0)
    up = np.roll(seed,-1,0)
    right = np.roll(seed,1,1)
    left = np.roll(seed,-1,1)
    up_right = np.roll(right,-1,0)
    up_left = np.roll(left,-1,0)
    down_right = np.roll(right,1,0)
    down_left = np.roll(left,1,0)
    return ( down + up + right + left + up_right + up_left 
           + down_right + down_left) 


# a silly and very inneficient vectorized version
from functools import partial

def loc_count(data, i, j) :
    s = data.shape
    return sum(data[i+m,j+n] for m in (-1, 0, 1) for n in (-1, 0, 1)
                     if (m != 0 or n != 0) and (i+m < s[0] and j+n < s[1]))

def neighbor_count_vec(seed) :
    s = seed.shape
    rows = np.arange(s[0]).reshape((s[0],1))
    cols = np.arange(s[1]).reshape((1,s[1]))
    loc_count_v =  np.vectorize(partial(loc_count,seed))
    return loc_count_v(rows, cols)
