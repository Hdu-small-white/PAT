
init_num = int(input())

init_content = []
for i in range(init_num):
    init_line = list(map(int, input().split()))
    init_content.append(init_line)

out_1 = 0
out_2 = 0
for i in init_content:
    if i[0] + i[2] == i[1] and i[0] + i[2] != i[3]:
        out_2 += 1
    if i[0] + i[2] != i[1] and i[0] + i[2] == i[3]:
        out_1 += 1

print(out_1, out_2)
