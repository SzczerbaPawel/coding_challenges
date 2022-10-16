def getSumOfDivisors(number):
    result = 0
    for i in range(1, number):
        if number % i == 0:
            result += i
    return result


result = 0

for i in range(2, 10000):
    d1 = getSumOfDivisors(i)
    d2 = getSumOfDivisors(getSumOfDivisors(i))
    if d2 == i and d1 != d2:
        # print(i, d1)
        result += i + d1

print(result/2)
