# # 실버3
# stack 이용

string = input()
ans = ""
stack = ""
tag = False


for i in string:
    if i == "<":
        tag = True
        ans += stack[::-1]
        stack = ""
        ans += i
        continue
    elif i == ">":
        tag = False
        ans += i
        continue
    # 빈칸 처리를 해줘야함
    elif i == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue

    if tag:
        ans += i
    else:
        stack += i
print(ans+stack[::-1])
