def facto(x):
    f=1
    while x>0:
        f=f*x
        x=x-1
    return f
x=int(input("enter number : "))
print("factorial of ",x," = ",facto(x))

