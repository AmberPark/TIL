import sys
sys.stdin = open("1260.txt", "r")

def dfs(v):
    visted[v] = 1 # 방문체크
    print(v, end=' ')
    for i in range(N+1):
        if visted[i] == 0 and arr[v][i] != 0:
            dfs(i)


def bfs(v):
    q = []
    q.append(v) # 시작점 넣고
    visted_2[v] = 1
    while q:
        t = q.pop(0)
        result.append(t)
        # visted_2[t] = 1
        for i in range(N+1):
            if visted_2[i] == 0 and arr[t][i]:
                q.append(i)
                visted_2[i] = 1



N, M, start = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
result = []
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

visted = [0] * (N+1)
visted_2 = [0] * (N+1) # 방문 기록할꺼 새로 초기화 해주고

dfs(start)
print()

bfs(start)
print(*result)
