def solution(name, yearning, photo):
    answer = []
    score = dict()

    for n, y in zip(name, yearning):
        score[n] = y

    for p in photo:
        tmp = 0
        for t in p:
            if t not in score:continue
            tmp += score[t]
        answer.append(tmp)

    return answer