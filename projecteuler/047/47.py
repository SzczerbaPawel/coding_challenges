from projecteuler.common_functions import is_prime


def has_exactly_four_distinct_prime_factors(primes, number):
    counter = 0
    for prime in primes:
        if number % prime == 0:
            counter += 1
            if counter > 4:
                return False
    if counter == 4:
        return True
    else:
        return False


primes = [2]
number = 3
result_counter = 0
while True:
    if has_exactly_four_distinct_prime_factors(primes, number):
        result_counter += 1
    else:
        result_counter = 0
    if is_prime(number):
        primes.append(number)
    if result_counter == 4:
        print(number-3)
        break
    number += 1
    