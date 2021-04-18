N = 5
R = 3

arr = [1,2,3,4,5]
sel = [0] * R

def combination(idx, sel_idx):
    if sel_idx == R:
        print(sel)
        return

    if idx == N:
        return
    sel[sel_idx] = arr[idx]
    combination(idx, sel_idx+1) # 뽑고가기
    combination(idx+1, sel_idx) # 안뽑고가기

combination(0, 0)