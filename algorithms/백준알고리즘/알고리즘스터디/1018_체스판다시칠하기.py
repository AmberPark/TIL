import sys
sys.stdin = open("1018.txt", "r")

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N-7):
    for j in range(M-7):
        pass