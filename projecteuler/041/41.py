import itertools

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def str_to_num(number):
    result = 0
    for digit in number:
        result = result * 10 + digit
    return result


digits = []
result = 0

for iter in range(1, 10):
    digits.append(iter)
    str_lst = list(itertools.permutations(digits))
    for number in str_lst:
        num = str_to_num(number)
        if num > result and is_prime(num):
            print(f"Largest print so far: {num}")
            result = num

print(result)
