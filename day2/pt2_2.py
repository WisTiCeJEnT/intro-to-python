x = int(input())
odd = 0
even = 0
while x > 0:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
    x = int(input())
print(f'Odd: {odd}, Even: {even}')
