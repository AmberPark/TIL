from collections import deque
computers = int(input())
pairs = int(input())
arr = [[0] * (computers+1) for _ in range(computers+1)]
cnt = 0
def BFS(n):
    global cnt
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        t = q.popleft()
        for i in range(computers+1):
            if visited[i] == 0 and arr[t][i] == 1:
                visited[i] = 1
                cnt += 1
                BFS(i)

for _ in range(pairs):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

visited = [0] * (computers+1)
BFS(1)
print(cnt)
