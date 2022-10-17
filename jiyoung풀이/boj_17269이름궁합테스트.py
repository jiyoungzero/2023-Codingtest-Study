# 문제 스스로 풀어보기 
# 리스트문제로도 풀리는지 딕셔너리로 풀어야 하는 지 잘 모르겠음 
# 획수를 내가 직접 넣어줘야 하는 건가?? 코딩으로 해결 할 수 있나.?


import sys
input = sys.stdin.readline

value_dic = {'A':3,
             "B" :2,
             "C":1,
             "D":2,
             "E":4,
             "F":3,
             "G":1,
             "H":3,
             "I":1,
             "J":1,
             "K":3,
             "L":1,
             "M":3,
             "N":2,
             "O":1,
             "P":2,
             "Q":2,
             "R":2,
             "S":1,
             "T":2,
             "U":1,
             "V":1,
             "W":1,
             "X":2,
             "Y":2,
             "Z":1}
n, m = map(int, input().split())
n_lst, m_lst = map(list, input().split())
two_lst = []


# 번갈아서 저장 
for i in range(min(n, m)):
    two_lst.append(n_lst[i])
    two_lst.append(m_lst[i])
    
if n>m: 
    i = n-m
    for ele in n_lst[m:m+i]:
        two_lst.append(ele)
else:
    i = m-n
    for ele in m_lst[n:n+i]:
        two_lst.append(ele)
    

temp = []

for i in range(len(two_lst)-1):
    temp.append(value_dic[two_lst[i]]+value_dic[two_lst[i+1]])
lst = temp

while len(lst) > 2:
    temp = []
    for i in range(len(lst)-1):
        v =lst[i]+lst[i+1]
        if v >= 10: temp.append(v%10)
        else: temp.append(v)
    lst=temp


# 한자리 퍼센트 나올경우.. 위에 while 문이 len(lst) > 2 해놔서
if lst[0] == 0:
    print(lst[1], end="")
    print("%")
else:
    for ele in lst:
        print(ele, end="")
    print("%")

        

        
    
    