fn=int(input("Enter the first number of the series: "))
sn=int(input("Enter the second number of the series: "))
n=int(input("Enter the number of terms needed: "))
print(fn,sn,end=" ")
while(n-2):
    tn=fn+sn
    fn=sn
    sn=tn
    print(tn,end=" ")
    n=n-1
