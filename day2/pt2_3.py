import random
ans = random.randint(1, 100)
n = int(input())
while n != ans:
    if n < ans:
        print(n, 'too LOW')
    else:
        print(n, 'too HIGH')
    n = int(input())

