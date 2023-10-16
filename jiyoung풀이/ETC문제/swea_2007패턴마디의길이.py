# 문제 스스로 풀어보기

T = int(input())

for t in range(1, T+1):
    lst = input()

    # 마디의 최대길이는 10
    # lst[:i+2] == lst[i+1:2*i+3] --> cocoa같은 경우 예외처리
    for i in range(10):
        if lst[:i+1] == lst[i+1:2*i+2] and lst[:i+2] == lst[i+1:2*i+3]:
            repeat = lst[:i+1]
            break
    
    
    
    print(f"#{t} {len(repeat)}")