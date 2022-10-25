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


def is_truncatable_from_left(i):
    number = i
    while len(str(number)) > 1:
        if is_prime(number) is not True:
            break
        else:
            power = len(str(number)) - 1
            number = number % 10 ** power
    condition = is_prime(number)
    return condition


def is_truncatable_from_right(i):
    number = i
    while len(str(number)) > 1:
        if is_prime(number) is not True:
            break
        else:
            number = number // 10
    condition = is_prime(number)
    return condition


result = 0
for i in range(9, 800000):
    if is_truncatable_from_left(i) and is_truncatable_from_right(i):
        print("Found truncatable prime: ", str(i))
        result += i
print(result)
