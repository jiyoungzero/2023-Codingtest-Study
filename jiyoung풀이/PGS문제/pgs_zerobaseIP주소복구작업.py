# 문제
# 당신은 네트워크 전문가로, 회사의 모든 IP 주소를 관리하고 있다.

# 어느날 신입으로 들어온 사원이 사색이 되어 진땀을 흘리고 있는 모습을 보게 되었다.

# 어깨너머로 보니 사내의 모든 IP주소에서 구두점(.)을 실수로 삭제한 것으로 보인다.

# 당신은 수작업으로 IP주소를 하나하나 복구하고 있는 신입 사원을 보고, 몰래 프로그램을 만들어 도와주기로 마음먹었다.

# 프로그램의 입력은 숫자만으로 이루어진 문자열이며(ex. "2552552551", "16819501"),

# 프로그램의 출력은 이 문자열에 .을 3개 끼워 넣어 가능한 모든 IP 주소를 나열한 배열이다. (ex. { "255.255.255.1"}. {"168.195.0.1", "168.19.50.1"})

# IP 주소의 각 숫자는 0 이상 255 이하의 숫자로만 이루어지며, 숫자 앞에 붙는 0(leading zero)는 허용되지 않는다.

# 위 조건에 맞는 프로그램을 작성하시오.

# 단, 결과 배열은 문자열 오름차순으로 정렬하여 출력하시오.

# 입력설명
# 4 <= s.length <= 12
# 출력설명
# 가능한 모든 IP주소를 문자열 배열로 출력

# 입출력 예시
# 입력
# s = "11011"

# 출력
# {"1.1.0.11", "1.10.1.1", "11.0.1.1"}

# 설명 - 가능한 점을 4개 찍을 수 있는 경우를 모두 나열하면 아래와 같다.

# {"1.1.0.11", "1.1.01.1", "1.10.1.1", "11.0.1.1"}

# 그런데, 이 중 "1.1.01.1"은 01에 leading zero가 있어서 허용되지 않는다.

def solution(s):
    addresses = []
    
    def is_promising(s):
        if len(s) == 0:
            return False
        if len(s) > 1 and s[0] == "0":
            return False
        if 0<= int(s) <= 255:
            return False
        return True    
    
    def make_address(s, dots):
        return s[:dots[0]]+"."+s[dots[0]:dots[1]] + "."+s[dots[1]:dots[2]]+"."+s[dots[2]:]
    
    
    def solve(s, dots):
        if len(dots) == 3:
            if is_promising(s[dots[2]:]):
                addresses.append(make_address(s, dots))
            return
        for i in range(1, 4):
            if len(dots) == 0:
                dots.append(i)
                if dots[-1] < len(s) and is_promising(s[:dots[0]]):
                    solve(s, dots)
            else:
                dots.append(dots[-1]+i)
                if dots[-1] < len(s) and is_promising(s[dots[-2]:dots[-1]]):
                    solve(s, dots)
                    
            dots.remove(dots[-1])
            
        

    solve(s, [])
    return sorted(addresses)