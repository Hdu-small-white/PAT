
dict_ = {1: 'yi', 2: 'er', 3: 'san', 4: 'si', 5: 'wu', 6: 'liu', 7: 'qi', 8: 'ba', 9: 'jiu', 0: 'ling'}

str_init = str(input())
sum_ = 0

for i in str_init:
    sum_ += int(i)

for i,j in enumerate(str(sum_)):
    if i + 1 == len(str(sum_)):
        print(dict_.get(int(j)))
    else:
        print(dict_.get(int(j)), end=' ')
        