def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for i in range(columns+1)] for j in range(rows+1)]
    num = 1
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            matrix[row][column] = num
            num += 1
            
    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1][y1]
        mini = tmp
        
        for k in range(x1,x2):
            test = matrix[k+1][y1]
            matrix[k][y1] = test
            mini = min(mini, test)

        for k in range(y1,y2):
            test = matrix[x2][k+1]
            matrix[x2][k] = test
            mini = min(mini, test)

        for k in range(x2,x1,-1):
            test = matrix[k-1][y2]
            matrix[k][y2] = test
            mini = min(mini, test)

        for k in range(y2,y1,-1):
            test = matrix[x1][k-1]
            matrix[x1][k] = test
            mini = min(mini, test)

        matrix[x1][y1+1] = tmp
        answer.append(mini)
            
    return answer