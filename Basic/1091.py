
init_num = int(input())

init_content = list(map(int, input().split()))

def is_j_num(base, multi):
    num = base**2*multi-base
    length_base = len(str(base))
    if length_base == 1:
        if num%10 == 0:
            return True
    elif length_base == 2:
        if num%100 == 0:
            return True
    elif length_base == 3:
        if num%1000 == 0:
            return True
    else:
        return False

for i in init_content:
    flag = False
    for j in range(1, 11):
        if is_j_num(i, j):
            print(j, i**2*j)
            flag = True
            break
    if flag == False:
        print("No")
