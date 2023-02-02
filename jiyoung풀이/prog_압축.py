# 문자열 구현

# start, end값이 변할 때는 while문으로 탈출문 잘 만들고, 마지막에 start = end-1 와 같이 업데이트 해주기

# def solution(msg):
#     answer = []
#     # 사전 초기화

        # 다른 사람 풀이중 좋은 것 -> zip 이용
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        dict = {}
        for c, idx in zip(alphabet, list(range(1,27))):
            dict[c] = idx

        
#     # dict = {
#     #     "A":1,
#     #     "B":2,
#     #     "C":3,
#     #     "D":4,
#     #     "E":5,
#     #     "F":6,
#     #     "G":7,
#     #     "H":8,
#     #     "I":9,
#     #     "J":10,
#     #     "K":11,
#     #     "L":12,
#     #     "M":13,
#     #     "N":14,
#     #     "O":15,
#     #     "P":16,
#     #     "Q":17,
#     #     "R":18,
#     #     "S":19,
#     #     "T":20,
#     #     "U":21,
#     #     "V":22,
#     #     "W":23,
#     #     "X":24,
#     #     "Y":25,
#     #     "Z":26
#     # }
#     tmp = 26
#     start, end = 0, 1
#     while end <= len(msg) :
#         c = msg[start:end]
#         if c in dict:
#             end += 1
#         else:
#             answer.append(dict[c[:-1]])
#             tmp += 1
#             dict[c] = tmp
#             start = end - 1

#     answer.append(dict[msg[start:end]])


#     return answer

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dict = {}
for c, idx in zip(alphabet, list(range(1,27))):
    dict[c] = idx
print(dict)