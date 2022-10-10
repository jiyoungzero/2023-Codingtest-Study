# 문제 스스로 풀어보기 

# 해시값을 출력하는 것
# 해당 알고리즘 개념이 없어서 학습 필요 -> hashlib 이용해야 할듯
# 18분 소요

import hashlib

data = input()
e = hashlib.sha256(data.encode())

result = e.hexdigest()
print(result)


# 정답코드 
# e = data.encode()
# result = hashlib.sha256(e).hexdigest()
# print(result)
