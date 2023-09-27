r,c,k = map(int,input().split())

A = [ list(map(int,input().split())) for _ in range(3) ]

def calR():

    global A

    new_graph = [] 

    for i in A:

        elem = set(i) # 한 행의 원소만 추출
        temt = [] # (원소, 갯수) 를 담을 그래프
        temt2 = [] # 새로운 행이 될 그래프
        for j in elem:
            if j==0:
                continue
            cnt = i.count(j)
            temt.append((j,cnt))

        temt.sort(key=lambda x:(x[1],x[0]))

        for k in temt:
            temt2.append(k[0])
            temt2.append(k[1])

        temt2 = temt2[:100] # 100개 제한

        new_graph.append(temt2)


    max_len = max(map(len,new_graph))

	# 빈 칸은 0만큼 채워준다.
    for i in range(len(new_graph)):
        while len(new_graph[i]) !=max_len:
            new_graph[i].append(0)

    A = new_graph


for i in range(101):

    try:
        if A[r-1][c-1]==k:
            print(i)
            break
    except:
        pass

    if len(A[0]) > len(A):
        A = list(map(list,zip(*A)))
        calR()
        A = list(map(list,zip(*A)))
    else:
        calR()

else:
    print(-1)