# 아이디어 생각 오래걸림
n = int(input())

ans = 0

for i in range(1, n+1):
    lst = list(map(int, str(i)))

    ans = i + sum(lst)

    if ans == n:
        print(i)
        break

    if i==n: # 생성자가 없어서 끝까지 탐색하면
        print(0)
