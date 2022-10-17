# 문제 스스로 풀어보기

# 32~
# 재귀함수 무조건 써야 할 듯 
# 크기의 반을 자르고 반을 자르고..해서 2*2 크기인 것부터 시작
# 왜 테스트케이스 답이 8이라 나오나.. --> r < size라고 해야 하는데, r <= size라고 했다..
# 50분 소요 / 30분 초과
import sys
input = sys.stdin.readline

N, r,c  = map(int, input().split())
size = 2**N



def Z(size, r, c):
    if size == 1: # 다 쪼갠거 
        return 0
    else:
        size //= 2 # 쪼개면 4개가 나오니까 각각을 재귀 돌리자..?
        if r < size and c < size:
            return Z(size, r, c)
        elif r < size and c >= size:
            return size*size + Z(size, r, c-size)
        elif r >= size and c < size:
            return 2*size*size + Z(size, r-size, c)
        elif r >= size and r >= size:
            return 3*size*size + Z(size, r-size, c-size)
        
            
print(Z(size, r, c))





