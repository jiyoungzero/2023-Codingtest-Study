# 분할정복 -> 이게 어딜 봐서 분할정복인지..?
import sys
input = sys.stdin.readline

# Moo(n) = Moo(n-1) + "m" + "o"*(n+2) + Moo(n-1)
# Moo(n)는 +를 기준으로 분할정복
# len(Moo(n-1)) = Moo(n)의 가운데 부분 빼고 // 2
# len(Moo(n-1)) = (len(Moo(n)) - len(n+3))//2
# 각 부분의 idx=N이 존재하면 그게 답 

search_idx = int(input())
result = 0

len_nth_moo = [3] # 초기화 "moo"
n = 0
nth_moo = 0 # 저기 위의 moo 수열길이 중 N을 포함하는 가장 작은 수열 찾기
while len_nth_moo[n] <= int(1e9):
    len_nth_moo.append(len_nth_moo[n]*2 +(n+3)+1) # ----> 처음으로 만들어지는 가운데가 mooo o:3개인데 n=0여서 틀림
    n += 1

for idx,ele in enumerate(len_nth_moo):
    if ele >= search_idx:
        nth_moo = idx
        break      
        
    
def Moo(idx, cur): # 찾는 idx, moo(k)의 k 
    if cur == 0:
        return "m" if idx==1 else 'o'
    
    tmp = (len_nth_moo[cur]-(cur+3))//2

    if 0 <= idx <= tmp:
        return Moo(idx, cur-1)
    elif (tmp) < idx <= (tmp+cur+3):
        return "m" if idx == tmp+1 else "o"
    else:
        idx -= (tmp+cur+3)# 여기 중요
        return Moo(idx, cur-1) 
        


print(Moo(search_idx, nth_moo))
    
