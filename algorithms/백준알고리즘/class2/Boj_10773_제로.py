n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
res = []
for i in range(n):
    res.append(lst[i])
    if res[-1] == 0:
        res.pop()
        res.pop()

print(sum(res))



