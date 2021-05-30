
list_index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

init_content = input()

out = []
for i in list_index:
    count = 0
    for j in init_content:
        if i == j:
            count += 1
    out.append(count)

for i,j in enumerate(out):
    if j != 0:
        print(str(i)+':'+str(j))
