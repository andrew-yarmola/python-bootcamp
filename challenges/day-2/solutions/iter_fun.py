import itertools as it

def count_odds(some_list):
    return sum([i%2 for i in some_list])

def sum_upto_even(some_list):
    return sum(it.takewhile(lambda x:x%2==1, some_list))

def triangle_num(n):
    return list(it.accumulate(range(n)))

def interleave_two(a,b):
    return list(it.filterfalse(lambda x: x is None, it.chain.from_iterable(it.zip_longest(a,b))))

def interleave(*data):
    # input is a sequence of listsx,
    return list(it.filterfalse(lambda x: x is None, it.chain.from_iterable(it.zip_longest(*data))))

def inversion_count(A):
    return len(list(filter(lambda x:x[0]>x[1],list(it.combinations(A,2)))))

def print_groupby(data, group_key):
    data = sorted(data, key=lambda x: x[group_key])
    for key, value in it.groupby(data, lambda x: x[group_key]):
        print(key)
        for item in value:
            print("    ", item)
