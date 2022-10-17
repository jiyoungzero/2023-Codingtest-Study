# 문제 스스로 풀어보기 

# 이전에 풀었던 거라 다시 복기해봄 --> 근데 스택으로도 풀 수 있을 것 같은데 좀 복잡할 듯 ㅠㅠ 풀이 찾아보자


import sys
input = sys.stdin.readline

words = list(input())
cnt, start = 0,0

while cnt < len(words):
    if words[cnt] == "<": # 이거는 그대로 지나가고
        cnt += 1
        while words[cnt] != ">":
            cnt += 1
        cnt += 1
    elif words[cnt].isalnum(): # 문자나 숫자일경우
        start = cnt 
        while cnt < len(words) and words[cnt].isalnum():
            cnt += 1
        r_words = words[start:cnt]
        r_words.reverse()
        
        words[start:cnt] = r_words
    else: # 공백
        cnt += 1
        
print(*words, sep="" )
        
    
    
    
    
