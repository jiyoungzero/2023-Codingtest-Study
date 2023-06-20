def solution(n, arr1, arr2):
    answer = []

    for a, b in zip(arr1, arr2):
        tmp = ""
        bin_a, bin_b = bin(a)[2:],bin(b)[2:]
        
        # 자릿수 맞추기
        for _ in range(n-len(bin_b)):
            bin_b = "0"+bin_b
        for _ in range(n-len(bin_a)):
            bin_a = "0" + bin_a

        for a, b in zip(bin_a, bin_b):
            if int(a) or int(b):
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)

    return answer