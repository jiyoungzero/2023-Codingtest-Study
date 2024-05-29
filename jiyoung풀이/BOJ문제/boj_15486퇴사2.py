import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    t, p = map(int, input().split())
    arr.append((t, p))