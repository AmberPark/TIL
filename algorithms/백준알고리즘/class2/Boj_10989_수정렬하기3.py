# 어렵네
import sys
n = int(input())
chk = [0] * 10001
for i in range(n):
    input_n = int(sys.stdin.readline())

    chk[input_n] += 1

for i in range(10001):
    if chk[i] != 0:
        for j in range(chk[i]):
            print(i)