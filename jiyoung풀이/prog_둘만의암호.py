# 문자열 

    ## 실패 -> 테스트케이스 오답
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # skip문자열을 alphabet에서 지우고 시작
#     for sk in skip:
#         alphabet = alphabet.replace(sk, "")

#     for c in s:
#         jump = (alphabet.index(c) + index) % len(alphabet)
#         s = s.replace(c, alphabet[jump])
# 정답 아효
def solution(s, skip, index):
    answer = ''
    alphabet = []
    
    for i in range(97, 123):
        if chr(i) in skip:
            continue
        alphabet.append(chr(i))

    for c in s:
        result = (alphabet.index(c) + index)
        if result >= len(alphabet):
            result = (result % len(alphabet)) 
        answer+=alphabet[result]
     
    return answer