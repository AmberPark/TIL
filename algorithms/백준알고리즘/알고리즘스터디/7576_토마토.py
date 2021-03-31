import sys
sys.stdin = open("7576.txt", "r")
from collections import deque
d = deque()
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

