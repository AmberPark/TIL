num = int(input())
lst = []
for _ in range(num):
    x, y = map(int, input().split())
    lst.append([x, y])
rank = 2
lank_list = [0] * num
for i in range(num-1):
    if lst[i][0] < lst[i+1][0] and lst[i][1] < lst[i+1][1]:
        # lank -= 1
        lank_list[i+1] = lank_list[i] - 1
    elif lst[i][0] > lst[i+1][0] and lst[i][1] > lst[i+1][1]:
        lank_list[i+1] = lank_list[i] + 1

    elif (lst[i][0] < lst[i+1][0] and lst[i][1] > lst[i+1][1]) or (lst[i][0] > lst[i+1][0] and lst[i][1] < lst[i+1][1]):
        lank_list[i]= rank
        lank_list[i+1] = rank

result = lank_list[::] # 복제
for v in lank_list:
    if lank_list.count(v) > 1:
        result[lank_list.index(v+1)] = lank_list.count(v) +lank_list[lank_list.index(v+1)] -1
# print(lank_list)
print(*result)

