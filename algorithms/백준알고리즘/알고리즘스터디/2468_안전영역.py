from collections import deque
N = int(input())
region = [list(map(int, (input().split()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
# 하나하나씩 돌아가면서 각 요소 이하까지 물이 차는 장마일때?  함수 돌리고 결과 스택에 넣어서 최대개수 출력하도록
def solve(n):
    global N, region, result, visited
    cnt = 0
    result = 0
    # 다시 초기화
    arr = region
    check = visited
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= n:
                arr[i][j] = 0
    # 싱우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                check[i][j] = 1
                for k in range(4):
                    ni = i + dr[k]
                    nj = j + dc[k]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] !=0 and check[ni][nj] == 0:
                        cnt += 1

                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] ==0: # 한칸만 안잠겼을때
                        result += 1
    if cnt > 1:
        result += 1


answer = deque()
for i in range(N):
    for j in range(N):
        rain = region[i][j]
        solve(rain)
        answer.append(result)

print(max(answer))
