# 카카오 채용연계형 인턴십 2021


# 내풀이..ㅋㅋㅋㅋㅋㅋ
def solution(s):
    dic = {"zero":0,"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    answer = ""
    tmp = ""
    for c in s:
        if tmp in dic.keys():
            answer += str(dic[tmp])
            tmp = ""
        if c.isalpha():
            tmp += c
        else:
            answer += str(c)
            
    if tmp in dic.keys():
        answer += str(dic[tmp])
    

    return int(answer)

# 다른 사람 풀이
def solution(s):
    words = ["zero","one","two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = ""
    
    for idx, word in enumerate(words):
        s = s.replace(word, str(idx))

    return int(s)