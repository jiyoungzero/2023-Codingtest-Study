# 카카오 2018 블라인드 채용 코테 1차 


# 구현 문제로...일단 6/4 -> time을 int로 변환한 거 부터가 안될 일이였다.
def solution(n, t, m, timetable):
    answer = ''
    n_timetable = []
    # 1. timetable을 오름차순으로 정렬
    # -> timetable에서 :를 기준으로 데이터를 나눈 다음에 int형으로 합치기 맨앞이 0이면 비포함
    for i in timetable:
        i = i.split(":")
        n_timetable.append(int(i[0])*100+int(i[1]))
    n_timetable.sort()

    
    
    # 2. 09:00시 부터 t간격으로 총 n회 운영하는데, 각 운영 마다 m명만 수용한다. 
    # 3. t간격 마다 m을 수용하는데, 900 <= timetable[i] <= 900 + t 이여야 m에 포함 가능11111
    # 셔틀버스 마지막 운영 시간 : 900 + (n-1)*t
    
    # n_cnt == n인데, len(tmp_ppl) < m이면, answer = time 
    # n_cnt == n인데, len(tmp_ppl) >= m이면, 가능한 애들은 다 들어가게 해놓고, answer = tmp_ppl[m-1]
    final_time = 900+(n-1)*int(t)
    if n == 1: 
        for time in range(900, final_time+1, t):
            tmp_ppl = []
            for i in range(len(n_timetable)):
                if n_timetable[i] <= time:
                    tmp_ppl.append(n_timetable[i])
            # 해당 시간에 포함된 사람만큼 n_timetable에서 삭제
            if len(tmp_ppl) >= m:
                n_timetable = n_timetable[m:]
            if len(tmp_ppl) < m: 
                n_timetable = n_timetable[len(tmp_ppl):]


            if len(tmp_ppl) < m:
                answer = time
            else:
                answer = tmp_ppl[m-1]-1
    
    
    elif n>1:
        n_cnt = 0
        for time in range(900, final_time+1, t):
            tmp_ppl = []
            for i in range(len(n_timetable)):
                if n_timetable[i] <= time:
                    tmp_ppl.append(n_timetable[i])
            # 해당 시간에 포함된 사람만큼 n_timetable에서 삭제
            if len(tmp_ppl) >= m:
                n_timetable = n_timetable[m:]
            if len(tmp_ppl) < m: 
                n_timetable = n_timetable[len(tmp_ppl):]
                
            n_cnt += 1

            if n_cnt == n:
                if len(tmp_ppl) < m:
                    answer = time
                else:
                    answer = tmp_ppl[m-1]-1
                

    
    
                
    # answer 후처리
    answer = str(answer)
    if len(answer) == 1:
        answer = "00:0"+answer
    elif len(answer) == 2:
        answer = "00:"+answer
    elif len(answer) == 3:
        answer = "0"+answer[0]+":"+answer[1:]
    else:
        answer = answer[:1]+":"+answer[1:]
                
    
    
    return answer



# 새롭게 알게 된 함수 , zfill(원하는 자릿수) -> 0으로 왼쪽을 채워줌

def solution(n, t, m, timetable):
    answer = 0
    
    # 모든 timetable을 *60로 환산
    n_timetable = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    n_timetable.sort()
    
    # 셔틀버스 도착 리스트
    bus_time = []
    for j in range(n):
        bus_time.append(9*60+t*j)
        
    i=0 # 다음에 버스에 오를 크루들의 인덱스, 다음 회차의 크루 인덱스를 바로 알 수 있음 
    for bt in bus_time:
        cnt = 0 # 버스에 타는 크루의 수
        while i<len(n_timetable) and cnt < m and n_timetable[i] <= bt  :
            i+=1
            cnt+=1
        
        if m>cnt: # 자리가 남으면
            answer = bt
        else: # 자리가 안남으면
            answer = n_timetable[i-1]-1
            
    # answer 후 처리
    hour = answer // 60
    minute = answer % 60
    
    return str(hour).zfill(2)+":"+str(minute).zfill(2)