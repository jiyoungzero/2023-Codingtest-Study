# greedy

def solution(lottos, win_nums):
    answer = []
    prize = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    checked = [False]*(6)
    # 11시 05분 부터 시작
    # lottos를 돌면서 win_nums에 있는지 세기 (0제외) -> checked 배열로 이미 있는것은 true로 만들기
    #  [len(checked) + len(0으로 된 경우), len(checked)]
    for idx, value in enumerate(lottos):
        if value in win_nums:
            checked[idx] = True 
    answer.append(prize[checked.count(True)+lottos.count(0)])
    answer.append(prize[checked.count(True)])

    return answer