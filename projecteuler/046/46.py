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


iter = 9
while True:
    if is_prime(iter):
        print(f"Skipping {iter} because it is prime")
        iter += 2
        continue
    print(f"Checking {iter}")
    condition = False
    square = 1
    while 2 * square * square < iter:
        if is_prime(iter - 2 * square * square):
            print(f"Condition met {iter} = {iter - 2 * square * square} + 2 * {square}^2")
            condition = True
            break
        square += 1
    if condition is False:
        print(iter)
        break
    iter += 2
