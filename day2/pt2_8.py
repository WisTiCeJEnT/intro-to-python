n = int(input())
is_prime = True
for i in range(2, n):
    # print(i, n%i)
    if n%i == 0:
        is_prime = False
# print(is_prime)
if is_prime:
    print(n, 'is a Prime Number')
else:
    print(n, 'is not a Prime Number')

