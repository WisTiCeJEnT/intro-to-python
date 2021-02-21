# เพิ่มสมาชิกให้กับ a เป็นเลขคู่ 1 - n
# a = [0, 2, 4, 6, 8, 10, ..., n]

n = int(input())
a = []
for i in range(n+1):
    if i%2 == 0:
        a.append(i)
print(a)

b = list(range(0, n+1, 2))
print(b)
# print(list(range(0, int(input())+1, 2)))

