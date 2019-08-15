import numpy as np
import random

def most_frequent(a):
    u, freq = np.unique(a, return_counts = True)
    return u[np.argmax(freq)]

def array_with_bincount(C):
    return np.repeat(np.arange(len(C)),C)
    
def distance_matrix(p) :
    return np.sqrt( np.sum( (p[:,np.newaxis] - p[np.newaxis,:])**2, axis = 2) ) 

def swap_cols(A,i,j):
    A[:,(i,j)] = A[:,(j,i)]

position = np.dtype([('x', 'int64'), ('y', 'int64')])
color = np.dtype([('r', 'int8'), ('g', 'int8'), ('b', 'int8')])
color_point = np.dtype([('position', position), ('color', color)])

def random_color_points(num_points):
  data = np.random.randint(0, 100, num_points)
  return data.astype(color_point)
