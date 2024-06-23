n,m, k=map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(k)]

def rotate():
    check = min(n, m)
    
    for cnt in range(check):
        tmp = matrix[cnt][cnt]
        
        n_max = n - cnt - 1
        m_max = m - cnt - 1
        
        # 1. 왼쪽 이동
        for j in range(m_max, cnt, -1):
            matrix[cnt][j-1] = matrix[cnt][j]
        
        # 2. 위쪽 이동 
        for i in range(n_max, cnt, -1):
            matrix[i-1][m_max] = matrix[i][m_max]
        
        
        # 3. 오른쪽 이동
        for j in range(cnt, m_max):
            matrix[cnt][j+1] = matrix[cnt][j]
        
        # 4. 아래쪽 이동 
        for i in range(cnt+1, n_max):
            matrix[i+1][m_max] = matrix[]
        
        # 5. tmp값 옮기기
        