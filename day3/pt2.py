n = int(input())
mn = None
mx = None
total = 0
for i in range(n):
    x = int(input())
    total = total + x
    if i == 0:      # ทำงานครั้งที่ 0
        mn = x
        mx = x
    else:           # ทำงานครั้งที่ 1-n
        if x < mn:
            mn = x
        if x > mx:
            mx = x
print(mn, mx, total/n)

