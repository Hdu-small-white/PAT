
init_content = input().split()

count_1 = 0
count_2 = 0
for i in init_content[0]:
    if i == init_content[1]:
        count_1 += 1
for i in init_content[2]:
    if i == init_content[3]:
        count_2 += 1

inter_1 = 0
inter_2 = 0
for i in range(count_1):
    inter_1 += int(init_content[1]) * 10 ** i
for i in range(count_2):
    inter_2 += int(init_content[3]) * 10 ** i

print(inter_1+inter_2)
