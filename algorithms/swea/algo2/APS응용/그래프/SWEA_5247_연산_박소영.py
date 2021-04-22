from collections import deque
# 뎈 안쓰니까 시간초과

def solve(n):
    global used, cnt
    q = deque()
    used = {}
    q.append((n, 0))
    # 이미 그 숫자가 나왔었으면 이제 그건 방문체크? 처럼 해야할것같은데

    while q:
        t, cnt = q.popleft()
        if used.get(t) == 1: # 그 숫자를 한번 썼을때 다음걸로 넘어가도록
            continue
        used[t] = 1

        if t == m:
            return cnt

        # 연산 4개 다 해봐
        if 1 <= t + 1 <= 1000000:
            # cnt += 1
            q.append((t + 1, cnt + 1))
        if 1 <= t - 1 <= 1000000:
            # cnt += 1
            q.append((t - 1, cnt + 1))
        if 1 <= t * 2 <= 1000000:
            # cnt += 1
            q.append((t * 2, cnt + 1))
        if 1 <= t - 10 <= 1000000:
            # cnt += 1
            q.append((t - 10, cnt + 1))


for tc in range(1, int(input()) +1):
    n, m = map(int, input().split())

    solve(n)
    # print(used)
    print('#{} {}'.format(tc, cnt))
