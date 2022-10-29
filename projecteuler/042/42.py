txt_file = open("p042_words.txt", "r")
file_content = txt_file.read()
content_list = file_content.split(",")
txt_file.close()


def pos(letter):
    return ord(letter) - 64


triangles = [n * (n + 1) / 2 for n in range(1, 1000)]
result = 0
for word in content_list:
    sum = 0
    for letter in word:
        sum += pos(letter)
    if sum in triangles:
        result += 1
print(result)
