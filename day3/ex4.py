# ให้รับข้อมูลเก็บใส่ตัวแปร a ทั้งหมด n ตัว
"""
input:
4
a
b
1
2
output:
['a', 'b', '1', '2']
"""
a = []
for i in range(int(input())):
    a.append(input())
print(a)

# print([input() for x in range(int(input()))])
