# 2019 카카오 기출

def solution(record):
    answer = []
    nickname = {}

    for r in record:
        tmp = r.split()
        if len(tmp) == 3:
            cmd, id, name = tmp
            nickname[id] = name

    for r in record:
        tmp = r.split()
        if tmp[0] == "Enter":
            name = nickname[tmp[1]]
            answer.append(name+"님이 들어왔습니다.")
        elif tmp[0] == "Leave":
            name = nickname[tmp[1]]
            answer.append(name+"님이 나갔습니다.")

    return answer