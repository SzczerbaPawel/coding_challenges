def check_if_the_same_digits(number1, number2):
    str1 = [int(digit) for digit in str(number1)]
    str2 = [int(digit) for digit in str(number2)]
    str1.sort()
    str2.sort()
    return str1 == str2


number = 0
while True:
    number += 1
    condition = True
    for i in range(2, 7):
        if not check_if_the_same_digits(number, i * number):
            condition = False
    if condition:
        print(f"Solution: {number}")
        break
