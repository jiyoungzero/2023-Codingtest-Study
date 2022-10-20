# 해시, 구현
# 하, 15분 (검색시간 포함)
# SHA-256 해시 알고리즘..? 처음 들어봐요.. 해시 정리하기
# 256bit, 64자리 문자열 반환
# 검색 후 5분만에 품
import hashlib
str = input()

result = hashlib.sha256(str.encode())
print(result.hexdigest())

# 정답과 동일함