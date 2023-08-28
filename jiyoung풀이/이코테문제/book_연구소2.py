# dfs(안전영역) + 완탐(최대안전영역을 위한 모든 경우의 수)

n, m = map(int, input().split())
data = [] # 초기 맵
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))
    
dx,dy = [0,0,1,-1],[1,-1,0,0]

result = 0

# dfs를 이용하여 바이러스(2)가 퍼지도록 만들기
# 현재 맵에서 안전 영역의 크기 계산하는 메서드
# dfs를 이용하여 울타리(3개) 설치 후, 매번 안전 영역 크기 계산 