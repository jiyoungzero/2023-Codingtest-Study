n, t = map(int, input().split())
r, c, d = map(str, input().split())
r, c = int(r), int(c)
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
dir_dict = {'U':2, 'L':3, 'R':0, 'D':1}

def in_range(a, b):
    return 1<=a<n+1 and 1<=b<n+1

d = dir_dict[d]
for _ in range(t):
    nr, nc = r+dxs[d], c+dys[d]
    if not in_range(nr, nc):
        d = 3 - d
        continue
    r = nr
    c = nc
print(r, c)
