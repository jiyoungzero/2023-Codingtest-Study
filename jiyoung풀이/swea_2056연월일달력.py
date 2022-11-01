import sys
input = sys.stdin.readline

T = int(input())


for t in range(1, T+1):
    result = ""
    date = input()
    
    dic = {1:31,
           2:28,
           3:31,
           4:30,
           5:31,
           6:30,
           7:31,
           8:31,
           9:30,
           10:31,
           11:30,
           12:31}
    
    y = date[0:4]
    m = date[4:6]
    d = date[6:]
    
    if 1<= int(m) <= 12 and int(d) <= dic[int(m)]:
        result = y+"/"+m+"/"+d
    else:
        result = -1
    
    
    print(f"#{t} {result}")