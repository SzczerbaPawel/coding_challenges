from num2words import num2words
import re

pattern = r'[^A-Za-z0-9]+'

result = 0
for i in range(1, 1001):
    word = num2words(i)
    sample_str = re.sub(pattern, '', word)
    print(str(result) + " + " + sample_str + " (" + str(len(sample_str)) + ") = " + str(result) + str(len(sample_str)))
    result += len(sample_str)
    print(result)
