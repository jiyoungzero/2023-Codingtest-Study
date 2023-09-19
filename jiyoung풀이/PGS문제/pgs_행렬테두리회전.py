def solution(rows, columns, queries):
    answer = []
    arr = [[ j*columns + i for i in range(1, rows+1)] for j in range(columns)]

    
    for a, b, c, d in queries:
        result = int(1e9)
        temp = arr[a-1][b-1]
        r, c = c - a + 1,  d - b + 1
        
        # 위로 올리기
        for j in range(a , c):
            arr[j-1][b-1] = arr[j][b-1]
            result = min(result, arr[j][b-1])
            
        
        # 왼쪽으로 옮기기
        for i in range(b, d):
            arr[c-1][i-1] = arr[c-1][i]
            result = min(result, arr[c-1][i])
            
        # 아래쪽으로 내리기
        for j in range(c-2, a-1, -1):
            arr[j+1][d-1] = arr[j][d-1]
            result = min(result, arr[j][d-1])
        
        # 오른쪽 일부만 옮기기
        for i in range(+1, -1):
            arr[a-1][i+1] = arr[a-1][i]
            result = min(result, arr[a-1][i])
        
        # 빈 곳 temp로 채우기
        arr[a-1][b] = temp
        result = min(result, temp)
        answer.append(result)
        
    return answer