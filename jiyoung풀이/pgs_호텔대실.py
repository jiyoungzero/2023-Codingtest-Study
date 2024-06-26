# 시간 다루기 
def timeToMinute(time):
    return int(time[0:2])*60+int(time[3:])

def prevAvail(arr, x):
    flag = True
    if x-10 >= 0:
        for i in range(x-10, x):
            if arr[i]:
                flag=False
                break
    else: return True
    return flag 

def afterClean(arr, x):
    for i in range(x, x+10):
        if arr[i] == False:arr[i] = True
            
def solution(book_time):
    answer = 0
    time_arr = [] # arr와 인덱스가 맞는 예약 시간 배열
    book_time.sort()
    start = timeToMinute(book_time[0][0])
    book_time.sort(key=lambda x:x[1])
    end = timeToMinute(book_time[-1][1])
    
    arr = [[False]*(end-start+11)] # 예약 가능한지 알아보기 위한 배열, +10한 이유는 뒤에 afterClean에서 인덱스 에러 안나도록
    print(start, end, len(arr[0]))
    
    # end - start + 1 +1 만큼의 길이를 가진 배열을 만듬

    
    # 각 time을 minute로 환산하고 start 값만큼 빼서 배열의 인덱스와 값을 맞춰줌    
    # 예약 시간 별로 for문을 돌면서
    # 예약 시간 이전 10분간 arr[i] == False한지 보기
    # 예약 시간 이후 10분간 arr[j] = True로 만들기 
    # 둘 중 하나라도 걸린다면 answer + 1
    for time in book_time:
        s = timeToMinute(time[0])
        e = timeToMinute(time[1])
        time_arr.append((s-start, e-start))
        
    for time in time_arr:
        print("d")
        # if time[0]-:
        for i in range(time[0], time[1]+1):
            if arr[i] == False:arr[i] = True
            else: 
                answer += 1
                continue
        # 이 후 청소시간도 체크처리
        afterClean(arr, time[1])

    return answer



## 누적합!! -> 겹치지 않도록 하는 문제에서는 누적합이 좋음 
def solution(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    return max(time_table)


# 그 외의 풀이 -> 우선순위 큐 이용
from heapq import heappop, heappush

def solution(book_time):
    answer = 1
    book_time_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time_ref.sort()

    heap = []
    for s, e in book_time_ref:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e+10)

    return answer
