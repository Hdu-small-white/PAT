"""
LEGE:04/29/2021
"""
num_init = int(input())

all_str_init = []
for i in range(num_init):
    line_init = input()
    all_str_init.append(line_init)

list_grade = []
for str_init in all_str_init:
    list_grade.append(int(str_init.split(' ')[2]))

index_max = list_grade.index(max(list_grade))
index_min = list_grade.index(min(list_grade))

print(all_str_init[index_max].split(' ')[0] + ' ' + all_str_init[index_max].split(' ')[1])
print(all_str_init[index_min].split(' ')[0] + ' ' + all_str_init[index_min].split(' ')[1])
