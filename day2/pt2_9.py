def my_is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True


n = int(input())
for i in range(2, n+1):
    if my_is_prime(i):
        print(i)

