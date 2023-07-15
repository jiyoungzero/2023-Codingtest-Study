# 정렬
# 우선순위 고려하기
import sys
input = sys.stdin.readline

n = int(input())
student = [] # 이름, 국, 영, 수 순으로
for i in range(n):
    name, kor, eng, math = map(str, input().split())
    student.append((name, kor, eng, math))

student = sorted(student, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in student:
    print(s[0])
