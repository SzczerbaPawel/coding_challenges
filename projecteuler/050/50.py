from projecteuler.common_functions import is_prime


biggest = 0
biggest_counter = 0
primes = [number for number in range(2, 5000) if is_prime(number)]
while len(primes) > 0:
    counter = 0
    sum = 0
    for prime in primes:
        counter += 1
        sum += prime
        if is_prime(sum) and sum < 1000000 and biggest_counter < counter:
            print(counter, sum)
            biggest = sum
            biggest_counter = counter
    primes.pop(0)


