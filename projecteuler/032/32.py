def checkNumber(number):
    result = False
    for j in range(1, number):
        if number % j == 0:
            # print(f"Checking {number} {j} {int(number/j)}")
            if checkPandigital(number, j, int(number/j)):
                print(f"Found number: {number}")
                return True
    return result


def checkPandigital(n1,n2,n3):
    number = str(n1)+str(n2)+str(n3)
    digits = []
    for digit in number:
        if digit in digits:
            return False
        else:
            digits.append(digit)
    goal = [str(x) for x in range(1, 10)]
    if goal == sorted(digits):
        return True
    else:
        return False


res = 0
for i in range(1000, 10000):
    if checkNumber(i):
        res = res + i

print(res)

