# using Sieve of Eratosthenes algorithm
n = int(input())
ans = list(range(2, n+1))
counter_ind = 0
while ans[counter_ind] ** 2 < n:
    current = ans[counter_ind]
    if current == -1:
        counter_ind += 1
        continue
    for i in range(counter_ind + current, n-1, current):
        ans[i] = -1
    counter_ind += 1
for i in ans:
    if i != -1:
        print(i)
