import sys
input = sys.stdin.readline

x, y = map(int, input().split())
dict = {1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
        }
day = ["MON","TUE","WED","THU", "FRI", "SAT", "SUN"]
# 해당 요일 - 1월 1일 빼고 며칠인지 계산 %7 나머지로

today = 0
if x != 1:
    for i in range(2, x):
        today+=dict[i]

if x == 1:today += (y-1)
else: today += (30+y)

print(day[today%7])