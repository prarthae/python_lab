color_1=input("enter colours separated by coma : ")
col_list_1=color_1.split(",")
color_2=input("enter colours separated by coma : ")
col_list_2=color_2.split(",")
print(col_list_1)
print(col_list_2)

res=list(set(col_list_1).difference(col_list_2))
print(res)

res_1=list(set(col_list_2).difference(col_list_1))
print(res_1)