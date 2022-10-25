def dec2bin(number):
    return bin(number).replace("0b", "")


def isPalindrome(num):
    # while num[-1] == "0":
    #     num = num[0:-1]
    while len(num) > 1:
        if num[0] != num[-1]:
            return False
        else:
            num = num[1:-1]
    return True


result = 0
for i in range(1, 1000001):
    if isPalindrome(str(i)) and isPalindrome(str(dec2bin(i))):
        result += i
        print(i, dec2bin(i))

print(result)
