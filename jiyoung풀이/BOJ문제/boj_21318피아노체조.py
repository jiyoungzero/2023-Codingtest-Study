import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    a, b = map(int, input().split())