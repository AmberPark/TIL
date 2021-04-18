import sys
sys.stdin = open("5177.txt", "r")

def heap_push(val):
    global idx
    idx += 1
    heap[idx] = val

    ch_idx = idx
    



for tc in range(1, int(input())+1):
    N = int(input())
    tree = list(map(int, input().split()))

    heap = [0] * (N+1)
    idx = 0

    for i in tree:
        heap_push(i)




