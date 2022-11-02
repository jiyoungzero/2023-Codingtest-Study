T = int(input())
dic = dict()

for i in range(ord('A'), ord('Z')+1):
    dic[chr(i)] = i-65
for i in range(ord('a'), ord('z')+1):  # 97
    dic[chr(i)] = i-65-6

dic.update({'0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57,
            '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63})

for t in range(1, T + 1):
    string = input()
    temp = ""
    for s in string:
        temp += "".join(format(dic[s], 'b').zfill(6))  # zfill 문자열 앞 0으로 채움
    ans = ""
    for i in range(0, len(temp), 8):
        ans += chr(int(temp[i:i + 8], 2))

    print("#{} {}".format(t, ans))


# 정답

# T = int(input())
# for t in range(1, T+1):
#     print(f'#{t} {b64decode(input()).decode("UTF-8")}')
