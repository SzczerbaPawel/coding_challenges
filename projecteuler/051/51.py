from projecteuler.common_functions import is_prime

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
limitted_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in range(1122, 1000000):
    if not is_prime(number):
        continue
    print(f"Checking prime number {number}")
    for digit in digits:
        if str(number).count(str(digit)):
            print(f"  Found digit {digit} in {number}")
            limitted_digits.remove(digit)
            counter = 0
            for limitted_digit in limitted_digits:
                if counter > 1:
                    break
                new_number = int(str(number).replace(str(digit), str(limitted_digit)))
                if is_prime(new_number):
                    print(f"    New number {new_number} is prime")
                else:
                    print(f"    New number {new_number} is not prime")
                    counter += 1
            if counter < 2:
                print("Found family")
                if number not in [4011, 4407, 7011]:
                    raise BaseException
            limitted_digits.append(digit)
        else:
            print(f"  Not found digit {digit} in {number}")
