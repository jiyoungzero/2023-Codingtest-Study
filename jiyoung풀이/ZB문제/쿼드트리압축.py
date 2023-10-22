answer = ''
def solution(img):

    n = len(img)

    def division(s_row, s_col, size):
        global answer
        flag = True
        if size == 1:
            answer += str(img[s_row][s_col])
            return 
        target = img[s_row][s_col]
        for i in range(s_row, s_row+size):
            for j in range(s_col, s_col+size):
                if img[i][j] != target:
                    flag = False
                    break
        if flag : 
            answer += str(target)
        if flag == False:
            answer += '('
            size //= 2
            division(s_row, s_col, size)
            division(s_row, s_col+size, size)
            division(s_row+size, s_col, size)
            division(s_row+size, s_col+size, size)
            answer += ")"
    division(0,0,n)

    return answer