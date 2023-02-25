# stack

def solution(arr):
    answer = []
    answer.append(arr[0])
    for ele in arr:
        if answer[-1] != ele:
            answer.append(ele)
    return answer