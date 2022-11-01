import itertools
from projecteuler.common_functions import is_prime


def are_permutations(a, b, c):
    return set(str(a)) == set(str(b)) and set(str(a)) == set(str(c))


for a in range(1488, 10000 - 3330 - 3330):
    b = a + 3330
    c = b + 3330
    if is_prime(a) and is_prime(b) and is_prime(c) and are_permutations(a, b, c):
        print(a, b, c, sep="")
