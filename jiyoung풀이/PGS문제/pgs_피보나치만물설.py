# 문제
# 만수는 연속된 두 수의 합이 계속되는 피보나치 수열이 너무나도 마음에 든 나머지, 세상에 숨어있는 모든 유사 피보나치 수열을 찾고자 한다.

# 여기서 유사 피보나치 수열은 피보나치 수열처럼 연속된 두 수의 합이 반복되지만, 첫 두 숫자는 자유롭게 선택할 수 있는 수열을 말한다.

# 숫자로 이루어진 문자열 nums가 있다고 할 때, 이것을 적절히 나누어 유사 피보나치 수열로 만들려고 한다.

# 예를 들어, nums = "14152944"로 문자열이 주어질 때, 이것을 유사 피보나치 수열로 나눈 결과는

# {14, 15, 29, 44} 이다.

# 위와 같이 동작하는 프로그램을 작성하시오.

# 단, 유사 피보나치 수열로 나눌 수 없는 경우 {}을 출력하고, 숫자를 나눌 때 숫자 앞에 앞선 0이(leading zero) 있어서는 안된다. (ex 03, 005 등으로 나눌 수 없다.)

# 또한, 각 숫자는 2^31 - 1(int 자료형의 최댓값)을 넘지 않아야 한다.

# 입력 설명
# 3 <= nums.length <= 10000
# 출력 설명
# 2^31 - 1이하의 정수로 이루어진 정수 배열


# 내풀이
def solution(nums):
    answer = []
    dp = []
    def dfs(idx):
        if idx == len(nums):
            answer.append(dp)
            return
        return

        for i in range(idx, len(nums)):
            print("ddddd")
            digit = nums[idx:i+1]
            if len(dp) > 2 and dp[-1] != dp[-2] + dp[-3]:
                return
            dp.append(digit)
            dfs(i+1)
            dp.pop()

    dfs(0)

    return answer

# 모범 답안
def solution2(num):
    def is_fibo(arr):
        return arr[-2] + arr[-3] == arr[-1]
    
    def backtracking(s, path):
        nonlocal res
        
        if s == "" and len(path) >=3 and is_fibo(path):
            res = path
            return
        for i in range(1, len(s) + 1):
            if (s[:i][0] == "0") and len(s[:i] != 1 ) or int(s[:i] > 2**31):
                return
            if len(path) >= 3 and not is_fibo(path):
                return
            backtracking(s[i:], path + [int(s[:i])])
            
    res = []
    backtracking(num, [])
    
    return res