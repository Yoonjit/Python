# LIFO, append, pop
# 4개 앞에서부터 넣기, 3개 뒤에서부터 빼기

a = ['K', 'o', 'r', 'e', 'a']
buff = []

for i in range(4):
    buff.append(a[i])

print('buff:', buff)

for i in range(3):
    print('pop >> ', end='')
    print(buff.pop())


# a = ['K', 'o', 'r', 'e', 'a']
# buff = []

# for x in a[:4]:
#     buff.append(x)

# for y in range(3):
#     print(buff.pop())