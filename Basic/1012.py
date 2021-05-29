
init_content = list(map(int, input().split()))

inter_1 = []
inter_2 = []
inter_3 = []
inter_4 = []
inter_5 = []
for i in init_content[1:]:
    if i % 5 == 0:
        inter_1.append(i)
    if i % 5 == 1:
        inter_2.append(i)
    if i % 5 == 2:
        inter_3.append(i)
    if i % 5 == 3:
        inter_4.append(i)
    if i % 5 == 4:
        inter_5.append(i)

out = []

if len(inter_1) != 0:
    out_1 = 0
    for i in inter_1:
        if i % 2 == 0:
            out_1 += i
    if out_1 == 0:
        out.append('N')
    else:
        out.append(out_1)
else:
    out.append('N')

if len(inter_2) != 0:
    out_2 = 0
    for i,j in enumerate(inter_2):
        if i % 2 == 0:
            out_2 += j
        else:
            out_2 -= j
    out.append(out_2)
else:
    out.append('N')

if len(inter_3) != 0:
    out.append(len(inter_3))
else:
    out.append('N')
if len(inter_4) != 0:
    out.append(round(sum(inter_4)/len(inter_4), 1))
else:
    out.append('N')
if len(inter_5) != 0:
    out.append(max(inter_5))
else:
    out.append('N')

for i,j in enumerate(out):
    if i != len(out)-1:
        print(j, end=' ')
    else:
        print(j)
