def fibo(n):
    n1,n2,i=0,1,0
    while(i<n):
        print(n1,end=" ")
        n1,n2=n2,n1+n2
        i+=1

n=int(input("Enter limit: "))
fibo(n)