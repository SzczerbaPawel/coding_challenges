def numberofDigits(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt


def cal(num):
    lst = []
    digit = numberofDigits(num)
    powTen = pow(10, digit - 1)

    for i in range(digit - 1):
        firstDigit = num // powTen

        left = (num * 10 + firstDigit -
                (firstDigit * powTen * 10))
        lst.append(left)

        num = left
    return lst


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


counter = 0
for number in range(2, 1000000):
    if is_prime(number):
        con = True
        for perm in cal(number):
            if not is_prime(perm):
                con = False
        if con:
            print("circular prime: " + str(number))
            counter += 1

print(counter)
