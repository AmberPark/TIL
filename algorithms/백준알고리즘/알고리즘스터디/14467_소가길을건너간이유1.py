import sys
sys.stdin = open("14467.txt", "r")

N = int(input())
cows = {}
cnt = 0

for i in range(N):
    number, road = map(int, input().split())
    if road != cows.get(number, road): # 찾으려는 key 값 없을때 미리 정해둔 default 값 구하려면 get(key, 'defalut value')
        cnt += 1
        cows[number] = road
    else:
        cows[number] = road

print(cnt)




