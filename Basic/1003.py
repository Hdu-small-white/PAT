"""
LEGE:04/29/2021
"""
num_init = int(input())

all_str_init = []
for i in range(num_init):
    init = input()
    all_str_init.append(init)

for str_init in all_str_init:
    num_P = str_init.count('P')
    num_A = str_init.count('A')
    num_T = str_init.count('T')
    index_P = str_init.find('P')
    index_T = str_init.find('T')

    if num_P + num_A + num_T == len(str_init) and num_A != 0:
        if num_P == 1 and num_T == 1 and index_T > index_P:
            if (index_T - index_P - 1) * index_P == len(str_init) - index_T - 1:
                print('YES')
                continue
    print('NO')
