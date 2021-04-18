def solve(s):
    global q, distance
    q.append(s)
    while q:
        t = q.pop(0)
        for i in range(v+1):
            if distance[i] == 0 and arr[t][i] == 1:
                q.append(i)
                distance[i] = distance[t] + 1

for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    arr = [[0] * (v+1) for _ in range(v+1)]
    q = []
    distance = [0] * (v + 1)
    for _ in range(e):
        a, b = map(int, input().split())
        arr[a][b] = arr[b][a] = 1

    s, g = map(int, input().split())

    solve(s)
    print('#{} {}'.format(tc, distance[g]))