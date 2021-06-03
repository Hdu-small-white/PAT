
init_content = list(map(int, input().split()))

inter_num = 0
out = 0

for i in init_content[1:]:
    if i > inter_num:
        out += 6 * (i-inter_num)
        inter_num = i
    else:
        out += 4 * (inter_num-i)
        inter_num = i

out += init_content[0] * 5

print(out)
