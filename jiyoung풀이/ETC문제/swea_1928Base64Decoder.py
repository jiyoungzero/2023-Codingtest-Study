# 문제 스스로 풀어보기 :  dlgo 

# import 했을 때20.
# import base64
# import sys
# input = sys.stdin.readline 


# T = int(input())

# for test_case in range(1, T+1):
#     result = 0
#     lst = input()
    
#     lst_decode = base64.b64decode(lst)
#     result = lst_decode.decode("ascii")
    
#     print(f"#{test_case} {result}")

# 해당 문자를 6자리의 2진수로 바꾼 후,
# 8자리씩 끊고 그것을 10진수로 바꾼다. 


def getBinaryNum(value):
    binaryNum = str(bin(value)[2:]) # 0b 제거
    # 6자리의 숫자로 바꾸어야 해서 
    while len(binaryNum) < 6:
        binaryNum = "0" + binaryNum
    return binaryNum

T = int(input())

# 초기화
base_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
base_lower = base_upper.lower()
dic = {}
tmp = -1
for i in base_upper:
    tmp += 1
    dic[i] = tmp
for i in base_lower:
    tmp += 1
    dic[i] = tmp
for i in range(10):
    tmp += 1
    dic[str(i)] = tmp
# 특수 문자 
dic['+'] = 62
dic['/'] = 63


for test_case in range(1, T+1):
    result = []
    
    lst = input()
    
    encode_lst = [] # 디코딩할 리스트
    for ele in lst:
        encode_lst.append(getBinaryNum(dic[ele])) # 이진수로 바꾼 encode_lst 를 만듦
    
    # 각각의 문자열 리스트를 하나의 문자열로 합치기
    encode_lst = "".join(encode_lst)

    # 8자리씩 끊어서 10진수 만들기
    for j in range(len(lst)*6//8):
        dex = int(encode_lst[j*8:j*8+8], 2)
        
        result.append(chr(dex))

    result = "".join(result)
    print(f"#{test_case} {result}")
    