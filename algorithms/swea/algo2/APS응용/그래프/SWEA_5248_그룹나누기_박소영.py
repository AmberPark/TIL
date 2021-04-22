def find_set(x): # 엑스 포함 집합을 찾는 오퍼레이션. 노드에서 루트까지 경로 찾으면서 노드의 부모정보 개신
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

for tc in range(1, int(input()) +1):
    n ,m = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = []
    p = [0] * (n + 1) # 인덱스 맞춰주기
    for i in range(1, n+1):
        p[i] = i
    for i in range(m):
        arr.append(lst[i*2:i*2+2])
        union(arr[i][0], arr[i][1])
    # print(arr)


    # 여기서 set 하면 안된다!! 루트를 찾아야하니까 이제 findset으로 x 를 포함하는 집합 찾기
    result = []
    for i in range(len(p)):
        result.append(find_set(i))
    # print(result)

    # 이제 중복제거
    ans = set(result)
    # print(ans)
    print('#{} {}'.format(tc, len(ans)-1))

    # for i in range(len(arr)):
    #     people[arr[i][0]][arr[i][1]] = people[arr[i][1]][arr[i][0]] = 1
    #
    # # print(people)
    # cnt = 0
    # plus = []
    # for i in range(len(people)):
    #     if sum(people[i]) > 0:
    #         cnt += 1
    #     if sum(people[i]) > 1:
    #         plus.append(sum(people[i])-1)
    #
    # result = 0
    # if plus:
    #     for i in plus:
    #         result = (cnt - i) // 2
    # else: # 겹치는게 없으면
    #     result = cnt // 2
    #
    #
    # if cnt != n:
    #     result += (n-cnt)
    # print('#{} {}'.format(tc, result))