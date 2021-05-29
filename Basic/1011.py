
init_num = int(input())

init_content = []
for i in range(init_num):
    init_line = list(map(int, input().split()))
    init_content.append(init_line)

for i in range(init_num):
    if init_content[i][0] + init_content[i][1] > init_content[i][2]:
        print("Case #"+ str(i+1) + ": true")
    else:
        print("Case #"+ str(i+1) + ": false")
