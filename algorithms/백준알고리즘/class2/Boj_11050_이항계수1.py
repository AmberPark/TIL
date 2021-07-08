n, k = map(int, input().split())
a = 1
for i in range(n, n-k, -1):
    a *= i
for j in range(k, 0, -1):
    a //= j

print(a)
