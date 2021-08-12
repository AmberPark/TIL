tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    target = lst[m]
    result = list(reversed(sorted(lst)))

    if lst.count(target) == 1:
        print(result.index(target) + 1)
    # else:
        









