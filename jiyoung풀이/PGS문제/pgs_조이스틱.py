# 기본 최소 이동 횟수는 길이 - 1
# 연속되는 A가 있을 때, 그것의 왼쪽이나 오른쪽부터 시작하며 알파벳을 변경하는 것이 가장 효율적이다.
# 때문에 (기존, 왼쪽부터 시작, 오른쪽부터 시작) 중에서 minimum이 답이다.
def solution(name):
    answer = 0
    cur_move = len(name) - 1

    for i, n in enumerate(name):
        answer += min(ord(n)-ord("A"), ord("Z")-ord(n)+1) # 상하이동수
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1
        cur_move = min(cur_move, 2*i+len(name)-next, i+2*(len(name)-next)) 
    answer += cur_move 

    return answer