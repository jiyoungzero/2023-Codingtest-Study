# 브론즈 2

cap, milk = [], []

for _ in range(3):
    a, b = map(int, input().split())
    cap.append(a)
    milk.append(b)

for i in range(100):
    if milk[i % 3] + milk[(i+1) % 3] > cap[(i+1) % 3]:
        temp = cap[(i+1) % 3] - milk[(i+1) % 3]
        milk[(i+1) % 3] += temp
        milk[i % 3] -= temp
    else:
        milk[(i+1) % 3] += milk[i % 3]
        milk[i % 3] = 0
print(*milk, sep='\n')
