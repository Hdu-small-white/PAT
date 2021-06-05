
index = {0: 'W', 1: 'T', 2: 'L'}
init_content = []
out = 1

for i in range(3):
    init_line = list(map(float, input().split()))
    init_content.append(init_line)

for i in init_content:
    print(index.get(i.index(max(i))), end=' ')
    out *= max(i)

out = (out * 0.65 - 1) * 2
print(round(out,2))
