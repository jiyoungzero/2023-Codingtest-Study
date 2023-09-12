def solution(x, y, n):
    def prep(nums, n):
        drop = len(nums) - n
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop()
                drop -= 1
            out.append(num)
        return out[:n]
    
    def merge(a, b):
        x = [max(a, b).pop(0) for _ in a+b]
        return x
    
    return max(merge(prep(x, i), prep(y, n-i))
            for i in range(n+1)
            if i <= len(x) and n-i <= len(y))
