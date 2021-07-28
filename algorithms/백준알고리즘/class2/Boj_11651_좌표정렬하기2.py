n = int(input())

lst = []
for _ in range(n):
    xy = list(map(int, input().split()))
    lst.append([xy[1], xy[0]])
# 람다쓰니까 시간초과
lst.sort()

for i in lst:
    print(i[1], i[0])
