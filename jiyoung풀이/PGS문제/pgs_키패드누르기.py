def solution(numbers, hand):
    answer = ''
    pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    l_pos, r_pos = [3,0],[3,2]

    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += "L"
            l_pos = [numbers[i]//3,0]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += "R"
            r_pos = [numbers[i]//3-1, 2]
        else:
            now_x, now_y = numbers[i]//3, 1
            if numbers[i] == 0:
                now_x, now_y = [3,1]
            l_dist = abs(l_pos[0] - now_x) + abs(l_pos[1]-now_y)
            r_dist = abs(r_pos[0] - now_x) + abs(r_pos[1]-now_y)
            print(l_dist, r_dist)
            if r_dist < l_dist:
                answer += "R"
                r_pos = [now_x, now_y]
            elif r_dist > l_dist:
                answer += "L"
                l_pos = [now_x, now_y]
            else:
                if hand[0] == "r":
                    answer += "R"
                    r_pos = [now_x, now_y]
                else:
                    answer += "L"
                    l_pos = [now_x, now_y]


    return answer
