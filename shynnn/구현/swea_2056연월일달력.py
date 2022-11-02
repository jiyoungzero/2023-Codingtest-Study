# D1

T = int(input())

for t in range(1, T+1):
    arr = list(map(int, input()))
    year = arr[0]*1000 + arr[1]*100 + arr[2]*10 + arr[4]
    month = arr[4]*10 + arr[5]
    day = arr[6]*10 + arr[7]

    if 1 > month or month > 12:
        print('#{} {}'.format(t, -1))
        continue
    else:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 10 or month == 12:
            if day < 1 or day > 31:
                print('#{} {}'.format(t, -1))
                continue
        elif month == 4 or month == 6 or month == 8 or month == 9 or month == 11:
            if day < 1 or day > 30:
                print('#{} {}'.format(t, -1))
                continue
        elif month == 2:
            if day < 1 or day > 28:
                print('#{} {}'.format(t, -1))
                continue

    print("#{} {}{}{}{}/{}{}/{}{}".format(t, arr[0], arr[1],
          arr[2], arr[3], arr[4], arr[5], arr[6], arr[7]))
