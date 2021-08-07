from collections import deque

q = deque()
ans = []

n, k = map(int, input().split())

for i in range(1, n+1):
    q.append(i)

while q:
    for i in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())

print('<', end="")
for i in range(len(ans)-1):
    print(ans[i], end='')
    print(', ', end='')
print(ans[-1], end='')
print('>')


