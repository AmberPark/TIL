arr = [1, 2, 3]
N = 3

sel = [0] * N # 결과들이 저장될 리스트
check = [0] * N # 해당 원소 이미 사용했는지 안했는지에 대한 체크

def perm(idx):
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1 # 사용했다.
                perm(idx+1)
                check[i] = 0 # 다음 반복문 위한 원상복구

perm(0)