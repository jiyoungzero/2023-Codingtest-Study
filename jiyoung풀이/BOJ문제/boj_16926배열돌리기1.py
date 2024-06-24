n,m, r=map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def rotate():
    check = min(n, m)
    
    for cnt in range(check//2):
        tmp = matrix[cnt][cnt]
        
        n_max = n - cnt - 1
        m_max = m - cnt - 1
        
        # 1. 왼쪽 이동
        for j in range(cnt, m_max):
            matrix[cnt][j] = matrix[cnt][j+1]

        # 2. 위쪽 이동 
        for i in range(cnt, n_max):
            matrix[i][m_max] = matrix[i+1][m_max]
        
        # 3. 오른쪽 이동
        for j in range(m_max, cnt, -1):
            matrix[n_max][j] = matrix[n_max][j-1]

        # 4. 아래쪽 이동 
        for i in range(n_max, cnt, -1):
            matrix[i][cnt] = matrix[i-1][cnt]

        
        # 5. tmp값 옮기기
        matrix[cnt+1][cnt] = tmp 
        
        
for _ in range(r):
    rotate()
    
for row in matrix:
    print(*row)
        