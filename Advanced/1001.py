
init = list(map(int, input().split()))
sum_ = init[0] + init[1]

if sum_ < 1000 and sum_ > -1000:
    print(sum_)

else:
    if sum_ > 0:
        str_sum = str(sum_)
        if len(str_sum) <= 6:
            print(str_sum[:-3] + ',' + str_sum[-3:])
        else:
            print(str_sum[0] + ',' + str_sum[1:4] + ',' + str_sum[-3:])
    else:
        str_sum = str(sum_)
        if len(str_sum) <= 7:
            print(str_sum[:-3] + ',' + str_sum[-3:])
        else:
            print(str_sum[0:2] + ',' + str_sum[2:5] + ',' + str_sum[-3:])
