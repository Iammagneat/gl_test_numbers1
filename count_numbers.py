with open('numbers.txt') as file:
    text_list = [line.rstrip() for line in file]
x = 0
for i in text_list:
    if not i.startswith('#'):
        x += float(i)
print(x)
