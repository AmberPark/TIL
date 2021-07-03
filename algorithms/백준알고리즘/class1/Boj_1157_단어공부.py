from collections import deque
s = list(input().upper())
new = list(set(s)) # 중복 제거 한 알파벳 리스트로 카운트 해줘야 시간초과 안남
n = {}
for i in new:
    n[i] = s.count(i)

cnt = deque()
for k, v in n.items():
    cnt.append(v)

if cnt.count(max(cnt)) >1:
    print('?')
else:
    print(max(n, key=n.get))

