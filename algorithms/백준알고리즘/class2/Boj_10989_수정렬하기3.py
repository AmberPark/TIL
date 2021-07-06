from collections import deque
n = int(input())
lst = deque()
for _ in range(n):
    lst.append(int(input()))

for i in sorted(lst):
    print(i)