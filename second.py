l1=[]
n=int(input("enter nomber of items in list-1: "))
print("\n")
for i in range (0,n):
    print("enter number at index",i)
    item=int(input())
    l1.append(item)
#print(l1)

l2=[]
m=int(input("enter the size of list_2: "))
print("\n")
for i in range(0,m):
    print("enter number at index ",i)
    item=(int(input()))
    l2.append(item)

print("list 1 : ",l1)
print("list 2 : ",l2)


if(len(l1)==len(l2)):
    print("List are of same size")
else:
    print("Length of lists are not same")
    print("length of list_1 : ",len(l1))
    print("length of list_2 : ",len(l2))

sum_1=0
for i in range(0,len(l1)):
    sum_1=sum_1+l1[i]

print("sum of l1 = ",sum_1)

sum_2=0
for i in range(0,len(l2)):
    sum_2=sum_2+l2[i]

print("sum of l2 = ",sum_2)

if sum_1==sum_2:
    print("Sum of elements of list are same ")
else:
    print("Sum of elements of list are not same ")


common=[x for x in l1 if x in l2]
print(common)