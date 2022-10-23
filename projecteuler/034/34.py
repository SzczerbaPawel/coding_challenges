def digitFactorial(digit):
    digit = int(digit)
    if digit == 0:
        return 1
    elif digit == 1:
        return 1
    elif digit == 2:
        return 2
    elif digit == 3:
        return 6
    elif digit == 4:
        return 24
    elif digit == 5:
        return 120
    elif digit == 6:
        return 720
    elif digit == 7:
        return 5040
    elif digit == 8:
        return 40320
    elif digit == 9:
        return 362880


def checkNumber(num):
    sum = 0
    for digit in str(num):
        sum += digitFactorial(digit)
    if sum == num:
        return True
    else:
        return False


result = 0

for number in range(10, 2540160):
    if checkNumber(number):
        result += number
        print(number)

print(result)