def perm(cnt):
    global result
    new = int(''.join(arr))
    if [new, cnt] in visited:
        return

    visited.append([new, cnt])

    if cnt == n:
        result = max(result, new)
        return


    for i in range(len(arr)-1):
        for j in range(i + 1, len(arr)):
            # 순서 바꾸고
            arr[i], arr[j] = arr[j], arr[i]
            perm(cnt + 1)
            # 원상복귀
            arr[i], arr[j] = arr[j], arr[i]


for tc in range(1, int(input()) + 1):
    num, n = input().split()
    arr = list(num)
    visited = []
    n = int(n)
    result = 0
    perm(0)
    print('#{} {}'.format(tc, result))

