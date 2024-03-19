#import sys
#sys.stdin = open("input.txt", "r")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def backtracking(cnt, tmp_numbers,swap_cnt):
    global visited, result
    if cnt == swap_cnt:
        tmp_numbers = "".join(tmp_numbers)
        if int(tmp_numbers) > int(result):
            result = tmp_numbers
        return 
    for i in range(len(tmp_numbers)):
        for j in range(i+1, len(tmp_numbers)):
            # 바꿀 때
            tmp_numbers[i], tmp_numbers[j] = tmp_numbers[j], tmp_numbers[i]
            if ("".join(tmp_numbers), cnt) not in visited:
                visited.append(("".join(tmp_numbers), cnt))
                backtracking(cnt+1, tmp_numbers, swap_cnt)
            
            tmp_numbers[i], tmp_numbers[j] = tmp_numbers[j], tmp_numbers[i]


for test_case in range(1, T + 1):
    result = "000000"
    visited = []
    numbers, swap_cnt = map(str, input().split())
    swap_cnt = int(swap_cnt)

    backtracking(0, list(numbers), swap_cnt)
    
    print(f"#{test_case} {result}")