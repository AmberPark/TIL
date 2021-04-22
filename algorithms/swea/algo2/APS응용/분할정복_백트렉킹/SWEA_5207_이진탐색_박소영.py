for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    cnt = 0

    for i in range(len(b)):
        if b[i] in a:
            now = 0
            left_idx = 0
            right_idx = n - 1
            while left_idx <= right_idx:
                mid = (left_idx + right_idx) // 2
                if a[mid] == b[i]: # 그 가운데 값이 찾던 값이면 카운트 하고 멈춰
                    cnt += 1
                    break

                elif a[mid] < b[i]: # 선택한게 찾는거보다 왼쪽에 있으면
                    # 오른쪽 구간 선택
                    left_idx = mid + 1
                    if now == 1: # 이미 오른족에 있엇으면 그만
                        break
                    now = 1 # 아니면 위치 오른쪽으로

                elif a[mid] > b[i]: # 오른쪽에 있으면
                    # 왼쪽 구간 선택
                    right_idx = mid - 1
                    if now == -1: # 이미 왼쪽족에 있었으면 그만
                        break
                    now = -1

    print('#{} {}'.format(tc, cnt))

