#  2022 카카오 tech 인턴십

def solution(survey, choices):
    answer = ''
    dic = {"R":0,"T":0, "C":0,"F":0, "J":0,"M":0, "A":0,"N":0}
    tmp = []

    for i,s in enumerate(survey):
        first, second = s[0], s[1]
        if choices[i] > 4:
            dic[second] += abs(choices[i]-4)
        elif choices[i] < 4:
            dic[first] += abs(choices[i]-4)
        else:continue

    cnt = 0
    for k, v in dic.items():
        cnt += 1
        tmp.append([k, v])
        if cnt == 2:
            if tmp[0][1] >= tmp[1][1]:
                answer += tmp[0][0]
            else:answer += tmp[1][0]
            cnt = 0
            tmp = []

    return answer