f = open('in.txt', 'r')
# print(f, type(f))
text = f.read()
# print(text, type(text))
a = text.split('\n')
# print(a)
a = a[0:-1]
print(a)
b = []
for i in range(len(a)):
    # print(a[i])
    b.append(int(a[i]))
print(b)
