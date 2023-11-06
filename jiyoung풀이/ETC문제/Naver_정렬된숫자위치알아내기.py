n = int(input())
arr = list(map(int, input().split()))
answer = []

s_arr = sorted(arr)

for ele in arr:
    for i in range(n):
        if s_arr[i] == ele:
            answer.append(i+1)
            s_arr[i] = -1 # 이미 방문 완료
            break
    

print(*answer)