import itertools


def str_to_num(number):
    result = ""
    for digit in number:
        result += str(digit)
    return result


lst = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

result = 0


def check_div(num):
    if int(num[1:4]) % 2 != 0:
        return False
    if int(num[2:5]) % 3 != 0:
        return False
    if int(num[3:6]) % 5 != 0:
        return False
    if int(num[4:7]) % 7 != 0:
        return False
    if int(num[5:8]) % 11 != 0:
        return False
    if int(num[6:9]) % 13 != 0:
        return False
    if int(num[7:10]) % 17 != 0:
        return False
    return True


for num in lst:
    str_number = str_to_num(num)
    if check_div(str_number):
        print(str_number)
        result += int(str_number)
print(result)
