import itertools as it

def count_odds(some_list) :
    return sum( i % 2 for i in some_list )

def count_odds_v2(some_list) :
    return sum(map(lambda x : x % 2, some_list))

def count_odds_v3(some_list) :
    return len(list(filter(lambda x : x % 2 == 1, some_list)))

def sum_upto_even(some_list) :
    return sum(it.takewhile(lambda x : x % 2 == 1, some_list))

def triangle_num(n) :
    return list(it.accumulate(range(n)))

def interleave_pair(a,b) :
    return list(it.chain.from_iterable(zip(a,b)))

def interleave(*data) :
    return list(it.chain.from_iterable(zip(*data)))

def interleave_longest(*data) :
    return list(filter(lambda x : x is not None, it.chain.from_iterable(it.zip_longest(*data))))

def inversion_count(A) :
    return sum( A[i] > A[j] for i,j in it.combinations(range(len(A)), 2)) 

def print_groupby(data, group_key) :
    data = sorted(data, key = lambda x : x[group_key])
    for key, items in it.groupby(data, lambda x : x[group_key]):
        print(key, *map(lambda item : '\n    ' + str(item), items))
