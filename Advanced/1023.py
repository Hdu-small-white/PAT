
init_content = int(input())
out_1 = init_content * 2

init_list = list(str(init_content))
out_list = list(str(out_1))

init_list.sort()
out_list.sort()

if init_list == out_list:
    print("Yes")
else:
    print("No")

print(out_1)
