ref = "vxrvip"
track = "xrviprvipvxrv"
ref_arr = []
answer = []
def findnDel(ref_arr, track):
    for i in ref_arr:
        if i in track:
            print(track)
            track =track.replace(i, "")
            print(track)
    return track

for i in range(len(ref)):
    for j in range(i, len(ref)):
        ref_arr.append(ref[i:j+1])
ref_arr = sorted(ref_arr, key=len)[::-1]

while len(track) != 0:
    for i in ref_arr:
        if i in track:
            track =track.replace(i, "")
            answer.append(len(i))

print(min(answer))
