n, k = map(int, input().split())

lst = [i for i in range(1, n+1)] * (1000//n)
res = []
print(lst)
for j in range(1, n+1):
    res.append(lst[k*j-1])
    lst.remove(lst[k*j-1])


    print(res)



