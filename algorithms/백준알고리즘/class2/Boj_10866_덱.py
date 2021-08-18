from collections import deque
import sys
input = sys.stdin.readline # 반복문으로 여러줄 입력 받는 사오항에서는 반드시 sys.stdin.readline() 사용해야 시간초과 발생 하지 않음
N = int(input())

q = deque()

for _ in range(N):
    order = list(input().split())
    if order[0] == 'push_front':
        q.appendleft(order[1])
    elif order[0] == 'push_back':
        q.append(order[1])
    elif order[0] == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif order[0] == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())

    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif order[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])