# easy

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# return : 가장 긴 갭 값 -> 다 1이면 0
def tenToBinary(N):
    result = ""
    while N >= 1:
        result += str(N%2)
        N //= 2
    return (result[::-1])
    



def solution(N):
    # Implement your solution here
    target = tenToBinary(N)
    answer = 0
    flag = False
    tmp = 0
    for i in range(1,len(target)):
        if target[i-1] == "1" and target[i] == "0":
            tmp += 1
            flag = True
        elif flag and target[i] == "0":
            tmp += 1
        elif flag and target[i] == "1":
            answer = max(answer, tmp)
            tmp = 0

    return answer