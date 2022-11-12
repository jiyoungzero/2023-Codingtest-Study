# 실버 5

S = list(map(int, input()))
result = []
# 4000만까지 연산 가능
# S의 길이는 100만 -> 1차원 배열 완탐 가능

for i in range(len(S)):
    if i == len(S)-1:
        result.append(S[i])
        # 마지막 요소는 전 것과 같든 다르든 무조건 넣어야함
        # 이전 값과 달라도 다르기 때문에 넣어야하고, 같아도 전값에서 안넣어주기 때문에 넣어야함
        continue
    if S[i] != S[i+1]:
        result.append(S[i])
print(min(result.count(0), result.count(1)))
