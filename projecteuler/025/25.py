def fib(number):
    if number == 1:
        return 1
    if number == 2:
        return 1
    return fib(number - 1) + fib(number - 2)

# print(fib(15))

n1 = 1
n2 = 1

i = 2

while len(str(n2)) < 1000:
    temp = n1 + n2
    n1 = n2
    n2 = temp
    i = i + 1
    print(i, temp)
