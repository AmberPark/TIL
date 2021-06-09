for tc in range(1, int(input()) + 1):
    N = int(input())
    num = map(int, input().split())
    lst = list(num)
    maxx = max(lst)
    minn = min(lst)

    print(f'#{tc} {maxx-minn}')