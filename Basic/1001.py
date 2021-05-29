
init = int(input())
count = 0

while init != 1:
    count += 1

    if init % 2 == 0:
        init /= 2
    else:
        init = (init * 3 + 1) / 2

print(count)
