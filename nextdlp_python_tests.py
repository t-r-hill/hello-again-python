from copy import copy

# Generates positive integers upto `upper_bound` which are multiples of `divisor``
def positive_integers(upper_bound: int, divisor: int):
    return None if upper_bound < 0 else (x for x in range(1, upper_bound + 1) if x % divisor == 0)

# Prints to console sum of positive integers divisble by 3 with a value less than 102030
print(sum(positive_integers(102030-1,3))) #1734969135

# Returns n lists using a comprehension in a `pythonic` style
def n_lists_comp(n: int):
    return [list(range(1,i+1)) for i in range(0,n+1) if i > 0]

# A more efficient implementation for n lists avoiding calling range for each iteration
def n_lists(n: int):
    result = []
    iterator = []
    for i in range(0,n):
        iterator.append(i+1)
        result.append(copy(iterator))
    return result
