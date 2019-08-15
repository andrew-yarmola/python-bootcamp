import numpy as np

def evolution(X) :
    nbrs_count = sum(np.roll(np.roll(X, i, 0), j, 1)
                     for i in (-1, 0, 1) for j in (-1, 0, 1)
                     if (i != 0 or j != 0))
    return (nbrs_count == 3) | (X & (nbrs_count == 2))

#def evolution(seed):
#    '''Conway's life two-dimensional turn logic
#    
#    given seed, returns next incremental step in Game of Life
#    '''
#
#    #Cheesy, perhaps, but it gets the job done
#    #These shift the array, up, down, right, left, etc.
#    down = np.roll(seed,1,0)
#    up = np.roll(seed,-1,0)
#    right = np.roll(seed,1,1)
#    left = np.roll(seed,-1,1)
#    upRight = np.roll(right,-1,0)
#    upLeft = np.roll(left,-1,0)
#    downRight = np.roll(right,1,0)
#    downLeft = np.roll(left,1,0)
#    
#    #adding all the shifted arrays together, overweighting original
#    s = (down + up + right + left + 
#              upRight + upLeft + downRight + downLeft + 10*seed)
#
#    #logic of the Game of Life
#    s[s==1] = 0
#    s[s==13] = 1
#    s[s==12] = 1
#    s[s==3] = 1
#    s[s!=1] = 0
#    
#    return s
