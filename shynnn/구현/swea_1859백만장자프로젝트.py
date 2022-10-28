# D2
# python 30초

# D2
# python 30초
# 테스트케이스 1개만 맞음..런타임에러
# T = int(input())
# for t in range(1, T+1):
#     num = int(input())
#     arr = list(map(int, input().split()))

#     result = []
#     answer = 0
#     last = arr[-1]
#     for item in arr:
#         # if not result:
#         #     continue
#         if item < last:
#             result.append(item)
#         else:
#             while result: # 여기서 런타임에러뜨는듯
#                 temp = item-result.pop()
#                 answer += temp
#     print('#'+str(t), answer)

# 정답
T = int(input())
for t in range(1, T+1):
    num = int(input())
    arr = list(map(int, input().split()))
    end = arr[-1]
    arr.reverse()  # 핵심.. 이걸 어케..하죠?
    cnt = 0
    for i in arr:
        if end > i:
            cnt += end-i
        else:
            end = i

    print('#'+str(t), cnt)
