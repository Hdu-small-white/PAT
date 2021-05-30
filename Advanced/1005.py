
index = {'0':"zero", '1':"one", '2':"two", '3':"three", '4':"four", '5':"five",
         '6':"six", '7':"seven", '8':"eight", '9':"nine"}

init_content = input()

out_sum = 0
for i in init_content:
    out_sum += int(i)

count = 0
for i in str(out_sum):
    if count < len(str(out_sum))-1:
        print(index.get(i), end=' ')
        count += 1
    
print(index.get(i))
