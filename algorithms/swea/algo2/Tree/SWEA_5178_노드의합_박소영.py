import sys
sys.stdin = open("5176.txt", "r")
def tree(n):
    if n <= N: # 인덱스 조건
        if lst[n]: # 그 노드번호에 값이 있으면
            return lst[n] # 그 값 리턴

        else:
            # 그 노드번호에 값이 없고 비어있으면 두개 더하는거 넣어주는데
            # 왼쪽 오른쪽 노드 반복이므로 여기서 재귀 사용
            lst[n] = tree(n*2) + tree(n*2+1) # 왼 + 오
            return lst[n] # 왼+오 한거 부모노드에 리턴
    # 인덱스 걸리면 0 리턴. 아니면 위에 왼 + 오 할때 int 랑 nonetype 더하려 한다고 에러 뜸
    return 0


for tc in range(1, int(input())+1):
    N, M, L = map(int,input().split())

    lst = [0] * (N+1)
    # 일단 노드 번호에 맞게 숫자 넣기
    for i in range(M):
        node, fig = map(int, input().split())
        lst[node] = fig

    print('#{} {}'.format(tc, tree(L)))

# 왜 절반만 맞는걸까. 오른쪽 노드 재귀 돌리면 왜 인덱스 에러가 나는걸까? 조건 걸어줬는데 왜?
# return.. 감 잡시는듯 알듯 아리까리