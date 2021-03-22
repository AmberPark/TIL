##########
# 책에서 봤었는데 기억 안나서 자괴감 들어하다가 결국 책 참고했습니다 ㅎㅎㅎㅎㅎ
# 코드 이해가 쉽게 안돼서 같이 이해해 보면 좋겠다 싶어 올립니다,,
##########
# 스택? 재귀?
# 일단 처음에 젤작은거를 3번으로 올리는건 같음.
N = int(input())
stk = []

def hanoi(number, start, end):
    if number > 1:
        # 3번 장대에 옮기기.
        # 장대 번호 합이 6 이니까 중간 기둥은 6-start-end로 구현할 수 잇음
        # 맨 밑에 원판 빼고 위에것 들을 그룹지어서 1장대에서 2장대로 옮기기
        hanoi(number-1, start, 6-start-end)
    # 1번 원판 까지 왔으면 프ㅣㄴ트
    stk.append([start, end])
    # print('{} {}'.format(start, end))
    if number > 1:
        # 그룹을 2장대에서 3장대로 옮기기
        hanoi(number-1, 6-start-end, end)

hanoi(N, 1, 3)

print(len(stk))
for i in range(len(stk)):
    print(*stk[i])