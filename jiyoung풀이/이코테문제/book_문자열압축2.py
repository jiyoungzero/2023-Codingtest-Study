# 카카오 신입 공채 문제 > 프로그래머스

# 풀이 : 문자열의 길이가 1000이하이기 때문에 가능한 모든 경우의 수를 탐색하는 '완전탐색'으로도 풀이가 가능


def solution(s):
    answer = 1001
    if len(s) == 1:
        return 1
    
    for step in range(1, len(s)+1):
        compressed = ""
        cnt = 1
        prev = s[:step]
        for j in range(step, len(s), step):
            nxt = s[j:j+step]
            if nxt == prev:
                cnt += 1
            else:
                if cnt >= 2:
                    compressed += (str(cnt) + prev)
                    cnt = 1
                else: 
                    compressed += prev
                prev = nxt
        # 남아있는 문자열 처리
        compressed += (str(cnt) + prev) if cnt >= 2 else prev 
        answer = min(answer, len(compressed))
    
    
    return answer