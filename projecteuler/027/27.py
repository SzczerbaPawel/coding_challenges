def fun(a, b, n):
    return (n * n) + (a * n) + b


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


result = 0
r1 = 0
rb = 0
for a in range(-999, 999):
    for b in range(-1000, 1000):
        n = 0
        while True:
            if is_prime(fun(a, b, n)):
                print("prime " + str(fun(a, b, n)))
                n = n + 1
            else:
                break
        # print(a, b, n)
        if n > result:
            result = n
            ra = a
            rb = b

print(result)
print(ra)
print(rb)
