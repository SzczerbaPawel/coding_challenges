txt_file = open("names.txt", "r")
file_content = txt_file.read()
print("The file content are: ", file_content)

content_list = file_content.replace('"', '').split(",")
txt_file.close()
content_list.sort()
print("The list is: ", content_list)


def getsum(str):
    sum = 0
    for letter in str:
        sum += ord(letter)-64
    return sum


result = 0

for idx, item in enumerate(content_list):
    result += getsum(item)*(idx+1)

print(result)





